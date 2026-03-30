import json
import os

from django.conf import settings
from django.core.management import BaseCommand


class ImportData(BaseCommand):
    model = None

    def handle(self, *args, **kwargs):
        file = os.path.join(
            settings.BASE_DIR, 'data', f'{self.model.__name__.lower()}.json'
        )
        try:
            with open(file, 'r') as file:
                data = json.load(file)

                if self.model.__name__ == 'Food':
                    for row in data:
                        additional_code = row.pop('additional', None)

                        obj, created = self.model.objects.update_or_create(
                            code=row.get('code'),
                            defaults=row
                        )
                        if additional_code:
                            add_item = self.model.objects.filter(
                                internal_code=additional_code
                            ).first()
                            if add_item:
                                obj.additional.add(add_item)
                else:
                    self.model.objects.bulk_create(
                        (self.model(**row) for row in data),
                        ignore_conflicts=True
                    )

                self.stdout.write(self.style.SUCCESS(
                    f'Загружено {len(data)}, '
                    f'{self.model._meta.verbose_name}!\n'
                    f'Из файла {file.name}'
                ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Ошибка {e}\n'
                f'Файл {file.name}\n'
            ))

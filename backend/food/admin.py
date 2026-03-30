from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.db.models import Count
from django.utils.safestring import mark_safe

from .models import Food, FoodCategory


admin.site.unregister(Group)
admin.site.unregister(User)


class FoodCostFilter(admin.SimpleListFilter):
    title = 'Стоимость'
    parameter_name = 'cost'

    TRESHOLD_1 = 100
    TRESHOLD_2 = 500
    MAX_PRICE = 10000

    LESS_ONE_HUNDRED = f'Меньше {TRESHOLD_1}(руб)'
    ONE_HUNDRED_TO_FIVE_HUNDRED = f'От {TRESHOLD_1}(руб) до {TRESHOLD_2}(руб)'
    MORE_FIVE_HUNDRED = f'Больше {TRESHOLD_2}(руб)'

    RANGES = {
        '1': ((0, TRESHOLD_1), LESS_ONE_HUNDRED),
        '2': ((TRESHOLD_1 + 1, TRESHOLD_2), ONE_HUNDRED_TO_FIVE_HUNDRED),
        '3': ((TRESHOLD_2 + 1, MAX_PRICE), MORE_FIVE_HUNDRED)
    }

    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        return [
            (
                key,
                "{} ({})".format(
                    text,
                    queryset.filter(cost__range=range_time).count()
                )
            )
            for key, (range_time, text) in self.RANGES.items()
        ]

    def queryset(self, request, recipes):
        if self.value() in self.RANGES:
            range_values, _ = self.RANGES[self.value()]
            return recipes.filter(cost__range=range_values)
        return recipes


class FoodInline(admin.StackedInline):
    model = Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name_ru', 'name_en', 'name_ch', 'order_id',
        'foods_count'
    )
    inlines = (FoodInline,)

    def get_queryset(self, request):
        return FoodCategory.objects.annotate(
            foods_count=Count('food')
        )

    @admin.display(description='Количество блюд')
    def foods_count(self, category):
        return category.foods_count


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name_ru', 'cost', 'category', 'display_additional'
    )
    list_filter = ('is_publish', 'is_vegan', 'is_special', 'category', FoodCostFilter)
    search_fields = ('name_ru',)
    list_prefetch_related = ('category',)

    @admin.display(description='Дополнительные товары')
    @mark_safe
    def display_additional(self, obj):
        return '<br>'.join(
            f'{food.name_ru}'
            for food in obj.additional.all()
        )

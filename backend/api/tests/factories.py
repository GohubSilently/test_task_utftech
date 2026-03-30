import factory

from food.models import Food, FoodCategory


class FoodCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodCategory

    name_ru = factory.Sequence(lambda n: 'Напитки_{}'.format(n))
    order_id = 10


class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Food

    name_ru = 'Чай'
    internal_code = factory.Sequence(lambda n: '{}00'.format(n))
    code = factory.Sequence(lambda n: n)
    cost = 123

from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from food.models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        prefetch_additional = Prefetch(
            'additional',
            Food.objects.filter(is_publish=True),
            'additional_foods'
        )
        published_foods = Food.objects.filter(is_publish=True).prefetch_related(
            prefetch_additional
        )
        return FoodCategory.objects.prefetch_related(
            Prefetch('food', published_foods, 'published_foods'),
        ).order_by('id')

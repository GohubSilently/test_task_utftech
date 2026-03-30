from django.urls import path

from .views import FoodListView


urlpatterns = [
    path('v1/foods/', FoodListView.as_view(), name='food-list')
]

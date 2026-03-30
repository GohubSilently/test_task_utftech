import pytest
from django.urls import reverse
from rest_framework import status

from .factories import FoodFactory, FoodCategoryFactory


@pytest.mark.django_db
def test_food_list_200(api_client):
    respone = api_client.get(reverse('food-list'))
    assert respone.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_many_categories(api_client):
    FoodCategoryFactory.create_batch(5)
    respone = api_client.get(reverse('food-list'))
    assert len(respone.data) == 5


@pytest.mark.django_db
def test_only_publish_food(api_client):
    category = FoodCategoryFactory()
    FoodFactory(category=category)
    FoodFactory(category=category, is_publish=False)
    respone = api_client.get(reverse('food-list'))
    data = respone.data[0]['foods']
    assert len(data) == 1
    assert data[0]['name_ru'] == 'Чай'


@pytest.mark.django_db
def test_additional_food(api_client):
    category = FoodCategoryFactory()
    tea = FoodFactory(category=category)
    additional_published = FoodFactory(category=category)
    additional_not_published = FoodFactory(category=category, is_publish=False)
    tea.additional.add(additional_published)
    tea.additional.add(additional_not_published)
    respone = api_client.get(reverse('food-list'))
    data = respone.data[0]['foods'][0]['additional']
    assert len(data) == 1
    assert data[0] == int(additional_published.internal_code)

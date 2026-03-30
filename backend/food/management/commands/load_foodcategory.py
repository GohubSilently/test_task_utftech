from .import_data import ImportData
from food.models import FoodCategory


class Command(ImportData):
    model = FoodCategory

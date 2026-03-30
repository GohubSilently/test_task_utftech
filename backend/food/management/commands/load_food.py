from .import_data import ImportData
from food.models import Food


class Command(ImportData):
    model = Food

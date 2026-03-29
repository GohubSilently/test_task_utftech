from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Food, FoodCategory

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Food)
admin.site.register(FoodCategory)

from django.contrib import admin
from .models import (
    Region,
    Category,
    Dish,
    State
)
# Register your models here.
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(State)
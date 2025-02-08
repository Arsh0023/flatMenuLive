from .dishes import (
    Dish,
    north_indian_vegetarian_dishes
)
import random

def getRandomDishes(num=3, region="North"):
    if region.lower() == "north":
        return [ Dish(d, getRecepieLink(d), region) for d in random.sample(north_indian_vegetarian_dishes, num)]

def getRecepieLink(dishName):
    return 'www.google.com'

print(getRandomDishes())
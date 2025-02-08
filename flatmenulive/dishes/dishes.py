import random
from .models import Dish

def getRandomDishes(num):
    dishes = Dish.objects.all()

    random_numbers = []
    while len(random_numbers) < num:
        random_numbers = list(random_numbers)
        random_numbers.append(random.randint(0,len(dishes)-1))
        random_numbers = set(random_numbers)

    return [dishes[r] for r in random_numbers]
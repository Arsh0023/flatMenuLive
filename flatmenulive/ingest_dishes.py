import os
import django
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flatmenulive.settings')
django.setup()

from dishes.models import (
    Dish,
    State,
    Region,
    Category
)

def populate_database():
    dishListf   = open('dishes.txt', 'r').readlines()
    dishList    = [ d.split(',') for d in dishListf ]
    lName       = 0
    lisVeg      = 1
    lCategory   = 2
    lRegion     = 3
    lState      = 4
    lLink       = 5
    
    for dish in dishList:
        region      = Region.objects.get(name=dish[lRegion])
        category    = Category.objects.get(name=dish[lCategory])
        state, _    = State.objects.get_or_create(name=dish[lState])

        createdDish, created = Dish.objects.get_or_create(
                name=dish[lName],
                defaults={
                    'isVeg': True if dish[lisVeg] == "True" else False,
                    'link': dish[lLink],
                }
            )
        
        createdDish.category.add(category)
        createdDish.region.add(region)
        createdDish.state.add(state)

        if created:
                print(f"Created Dish: {dish[lName]}")
        else:
            print(f"Dish {dish[lName]} already exists")
    
if __name__ == "__main__":
    populate_database()
    print("Database populated successfully!")
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .dishes import getRandomDishes

numOfDishes = 3

# Create your views here.
def index(request):
    print(getRandomDishes(numOfDishes))
    return render(request, 'index.html', {
        'dishes': getRandomDishes(numOfDishes)
    })
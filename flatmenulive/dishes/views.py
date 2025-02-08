import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getDish import getRandomDishes

numOfDishes = 3

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'dishes': getRandomDishes(numOfDishes)
    })
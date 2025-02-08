from django.db import models

# Create your models here.
class Region(models.Model):
    name       = models.CharField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return f"{self.name}"

class State(models.Model):
    name       = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    name       = models.CharField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

class Dish(models.Model):
    name       = models.CharField(max_length=100, unique=True, null=False)
    isVeg      = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category   = models.ManyToManyField(Category)
    region     = models.ManyToManyField(Region)
    state      = models.ManyToManyField(State)
    link       = models.CharField(max_length=256, blank=True, default="Provide link")

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f"{self.name}"
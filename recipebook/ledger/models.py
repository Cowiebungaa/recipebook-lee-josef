from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.pk])
    
    
class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE, 
        related_name='recipe')
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='ingredients')
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return "{} {} for {}".format(self.quantity, self.ingredient, self.recipe.name)
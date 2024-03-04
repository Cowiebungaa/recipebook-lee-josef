from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'ledger/recipe_details.html', {'recipe': recipe})
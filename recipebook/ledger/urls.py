from django.urls import path
from .views import recipe_list, recipe_detail

app_name = "ledger"

urlpatterns = [
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>', recipe_detail, name='recipe_detail'),
]

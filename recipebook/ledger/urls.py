from django.urls import path
from .views import recipe_list, recipe_1, recipe_2 

app_name = "ledger"

urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
    path('1/', recipe_1, name='recipe1_detail'),
    path('2/', recipe_2, name='recipe2_detail'),
]
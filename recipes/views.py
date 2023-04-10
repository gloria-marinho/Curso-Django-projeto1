from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

recipes = Recipe.objects.filter(is_published=True).order_by('-id')

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
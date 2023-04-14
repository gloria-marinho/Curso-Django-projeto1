from django.shortcuts import get_list_or_404
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

def home(request):
   recipes = Recipe.objects.filter(
      is_published=True
      ).order_by('-id') 
   return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
def category(request, category_id):
   recipes = get_list_or_404(
      Recipe, category_id=category_id,
      is_published=True,
      ).order_by('-id')
   
   return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category_name} - Category | '
    })

def recipe(request, id):
    recipes = Recipe.objects.filter(
       pk=id,
      is_published=True
      ).order_by('-id')-first() 
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
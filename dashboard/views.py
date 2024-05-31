from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from recipe.models import Recipe


@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(created_by=request.user)

    return render(request, 'dashboard/myrecipes.html', {
        'recipes': recipes
    })

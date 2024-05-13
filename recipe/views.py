from django.shortcuts import render, get_object_or_404

from .models import Recipe


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(pk=pk)[:3]

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'related_recipes': related_recipes
    })
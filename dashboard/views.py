from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from recipe.models import Recipe
from .models import Wishlist


@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(created_by=request.user)

    return render(request, 'dashboard/myrecipes.html', {
        'recipes': recipes
    })


@login_required
def my_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)

    return render(request, 'dashboard/mywishlist.html', {
        'wishlist': wishlist[0].recipes.all()
    })


@login_required
def add_to_wishlist(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist[0].recipes.add(recipe)


    return redirect('dashboard:my_recipes')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import NewRecipeForm, EditRecipeForm


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(pk=pk)[:3]

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'related_recipes': related_recipes
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()

            return redirect('recipe:detail', pk=recipe.id)

        
    else:
        form = NewRecipeForm()

        return render(request, 'recipe/form.html', {
            'form': form,
            'title': 'New Recipe'
        })
    

@login_required
def delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)

    recipe.delete()

    return redirect('dashboard:my_recipes')


@login_required
def edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    print(request)
    if request.method == "POST":
        print("inside if")
        form = EditRecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()

            return redirect('recipe:detail', pk=recipe.id)

    else:
        form = EditRecipeForm(instance=recipe)

        return render(request, 'recipe/form.html', {
            'form': form,
            'title': 'Edit Recipe'
        })
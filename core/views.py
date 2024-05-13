from django.shortcuts import render, redirect
from .forms import SignupForm

from recipe.models import Recipe, Category


def home(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'recipes': recipes,
        'categories': categories
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
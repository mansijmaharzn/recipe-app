from django.urls import path

from . import views

app_name = 'dashboard'


urlpatterns = [
    path('my-recipes/', views.my_recipes, name='my_recipes'),
]
from django.urls import path

from . import views

app_name = 'dashboard'


urlpatterns = [
    path('my-recipes/', views.my_recipes, name='my_recipes'),
    path('<int:pk>/add-to-wishlist', views.add_to_wishlist, name='add_to_wishlist'),
    path('my-wishlist/', views.my_wishlist, name='my_wishlist'),
]
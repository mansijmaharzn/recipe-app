from django.urls import path

from . import views

app_name = 'recipe'


urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('new/', views.new, name='new'),
]
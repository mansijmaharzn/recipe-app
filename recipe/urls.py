from django.urls import path

from . import views

app_name = 'recipe'


urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('move_cars/<int:pk>/', views.move_cars, name='move_cars'),
    path('view/', views.view_cars, name='view_cars')
    ]
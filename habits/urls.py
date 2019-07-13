from django.urls import path
from . import views

urlpatterns = [
    path('habit/', views.habit_list),
    path('habit/<int:pk>/', views.habit_detail),

]

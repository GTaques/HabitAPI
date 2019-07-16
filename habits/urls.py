from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list),
    path('habit/<int:pk>/', views.habit_detail),

]

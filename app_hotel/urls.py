from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('<int:pk>/', views.ItemsView.as_view())
]
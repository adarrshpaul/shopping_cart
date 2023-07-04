from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuView.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.books),
    path('', views.Books.as_view()),
    path('<int:pk>',views.Book.as_view())    
]
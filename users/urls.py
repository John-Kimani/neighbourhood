from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.home_news, name='home-news'),
]
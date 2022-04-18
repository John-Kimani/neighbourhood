from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('hood/', views.neighboorhood, name='hoodpage'),
    path('business/', views.business, name='businesspage'),
]
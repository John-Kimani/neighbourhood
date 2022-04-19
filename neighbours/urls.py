from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('hood/', views.neighboorhood, name='hoodpage'),
    path('hood/view/<int:neighborhood_id>', views.view_hood, name='singlehood'),
    path('hood/join/', views.join_hood, name='joinhood'),
    path('business/', views.business, name='businesspage'),
    path('business/register/', views.register_business, name='registerbusiness'),
]
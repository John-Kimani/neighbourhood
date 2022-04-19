from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    #hood
    path('hood/', views.neighboorhood, name='hoodpage'),
    path('hood/view/<int:neighborhood_id>', views.view_hood, name='singlehood'),
    path('hood/join/', views.join_hood, name='joinhood'),
    #business
    path('business/', views.business, name='businesspage'),
    path('business/register/', views.register_business, name='registerbusiness'),
    path('business/view/<int:business_id>', views.view_business, name='singlebusiness'),
    #post
    path('timeline/', views.timeline, name='timeline'),
]
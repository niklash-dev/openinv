from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('inventory/', views.inventory, name='inventory'),
    path('container/', views.container, name='container'),
    path('location/', views.location, name='location'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
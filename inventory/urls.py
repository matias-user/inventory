from django.urls import path
from .views.common import home, redirect_home
from .views.inventory import all_inventory

app_name = 'inventory'
urlpatterns = [
    path('', redirect_home),
    path('home/', home, name='home' ),
    path('inventory/', all_inventory, name='inventory' )
]

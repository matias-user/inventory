from django.urls import path
from .views.common import home, redirect_home
from .views.inventory import all_inventory, create_or_update

app_name = 'inventory'
urlpatterns = [
    path('', redirect_home),
    path('home/', home, name='home' ),
    path('inventory/', all_inventory, name='inventory' ),
    path('create/', create_or_update, name='create' ),
    path('update/<product_id>/', create_or_update, name='update' ),
]

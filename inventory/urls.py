from django.urls import path
from .views.common import home, redirect_home
from .views.inventory import all_inventory, create_or_update_product, create_or_update_supplier

app_name = 'inventory'
urlpatterns = [
    path('', redirect_home),
    path('home/', home, name='home' ),
    path('inventory/', all_inventory, name='inventory' ),
    path('create_product/', create_or_update_product, name='create_product' ),
    path('update/<product_id>/', create_or_update_product, name='update' ),
    path('create_supplier/', create_or_update_supplier, name='create_supplier' ),
]

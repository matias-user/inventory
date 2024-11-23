from django.urls import path
from .views import home, redirect_home

app_name = 'inventory'
urlpatterns = [
    path('', redirect_home),
    path('home/', home, name='home' )

]

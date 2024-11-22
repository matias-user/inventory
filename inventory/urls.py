from django.urls import path
from .views import home

app_name = 'inventory'
urlpatterns = [
    path('home/', home, name='home' )
]

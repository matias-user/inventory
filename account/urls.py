from django.urls import path
from .views.register import register

app_name= 'account'
urlpatterns = [
        path('register/', register, name='register')

]
from django.urls import path
from .views.register import register
from .views.login import login_user

app_name= 'account'
urlpatterns = [
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
]

from django.urls import path
from .views.register import register
from .views.login import login_user
from django.contrib.auth.views import LogoutView

app_name= 'account'
urlpatterns = [
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', LogoutView.as_view(next_page='/home'), name='logout')
]

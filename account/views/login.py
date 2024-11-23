from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('inventory:home')
        else:
            messages.error(request, 'Hubo un error en el usuario o contraseña!')
            return render(request, 'login/login.html')
    else:

        return render(request, 'login/login.html')

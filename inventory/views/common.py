from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    return render(request, 'inventory/home.html')

def redirect_home(request):

    return redirect('inventory:home')
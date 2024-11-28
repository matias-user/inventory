from django.shortcuts import render


def all_inventory(request):


    return render(request, 'inventory/inventory.html')


def create(request):


    return render(request, 'inventory/create.html')
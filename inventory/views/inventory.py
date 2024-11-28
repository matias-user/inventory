from django.shortcuts import render


def all_inventory(request):


    return render(request, 'inventory/inventory.html')
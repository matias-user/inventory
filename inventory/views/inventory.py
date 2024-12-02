from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ProductoForm
from ..models import Product


def all_inventory(request):

    products = Product.objects.all()[:20]

    return render(request, 'inventory/inventory.html', {'products': products })


def create_or_update(request, product_id=None):

    if product_id is not None:
        product = get_object_or_404(Product, pk=product_id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')
    else:
        print(product)
        form = ProductoForm(instance=product)


    return render(request, 'inventory/create_or_update.html', {'form':form, 'product':product})
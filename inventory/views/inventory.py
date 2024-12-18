from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ProductoForm, SupplierForm
from ..models import Product, Supplier


def all_inventory(request):

    products = Product.objects.all()[:20]

    return render(request, 'inventory/inventory.html', {'products': products })


def create_or_update_product(request, product_id=None):

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
        form = ProductoForm(instance=product)


    return render(request, 'inventory/create_or_update_product.html', {'form':form, 'product':product})


def create_or_update_supplier(request, supplier_id=None):

    if supplier_id is not None:
        supplier = get_object_or_404( Supplier, pk=supplier_id )
    else:
        supplier = None

    if request.method == 'POST':
        form = SupplierForm( request.POST, instance=supplier )

        if form.is_valid():
            supplier.save()
            return redirect('inventory:inventory')
    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'inventory/create_or_update_supplier.html', {'form':form})
        
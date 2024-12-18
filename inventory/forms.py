from django import forms
from .models import Product, Supplier


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['supplier','category']

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__' 
from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField( blank=False, max_length=255, verbose_name='Nombre' )
    contact_number = models.CharField( max_length=255, verbose_name='Número de contacto' )
    email = models.CharField( blank=False ,max_length=255, verbose_name='Correo electrónico' )
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField( blank=False, max_length=100, verbose_name='Nombre' )
    description = models.CharField( blank=True, null=True , verbose_name='Descripción', max_length=255 )

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField( blank=False, max_length=100, verbose_name='Nombre' )
    description = models.CharField( blank=True, null=True , verbose_name='Descripción', max_length=255 )
    price = models.DecimalField( max_digits=10, decimal_places=2, verbose_name='Precio' )
    # category = models.ForeignKey( Category, on_delete=models.CASCADE, verbose_name='Categoría' )
    # supplier = models.ForeignKey( Supplier, on_delete=models.CASCADE, verbose_name='Proveedor' )

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización")

    # def __str__(self):
    #     return f"{self.name} - {self.category.name}"
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
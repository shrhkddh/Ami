from django.db import models

class ProductSize(models.Model):
    size = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_sizes'

class Product(models.Model):
    name         = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=20, decimal_places=4)
    created_at   = models.DateTimeField(auto_now_add=True)
    guide        = models.CharField(max_length=500, null=True)
    product_size = models.ForeignKey('ProductSize', on_delete=models.SET_NULL, null=True)
    type_name    = models.ForeignKey('menu.TypeName', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'products'

class Color(models.Model):
    name         = models.CharField(max_length=500)
    button_color = models.URLField(max_length=2000, default = '')
    product      = models.ManyToManyField('Product', through = 'ProductColor')

    class Meta:
        db_table = 'colors'

class ProductColor(models.Model):
    color   = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_colors'

class ProductImage(models.Model):
    image_url     = models.URLField(max_length=2000)
    product_color = models.ForeignKey('ProductColor', on_delete=models.CASCADE, default = '')

    class Meta:
        db_table = 'product_images'

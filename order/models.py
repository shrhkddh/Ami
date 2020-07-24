from django.db import models

class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_status'

class Order(models.Model):
    cart_bag     = models.IntegerField()
    address      = models.CharField(max_length=400)
    created_at   = models.DateTimeField(auto_now_add=True)
    guest        = models.ForeignKey('account.Guest', on_delete=models.SET_NULL, null=True)
    account      = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class OrderProduct(models.Model):
    order    = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    product  = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'order_products'

class CartWishlist(models.Model):
    product = models.ForeignKey('product.ProductColor', on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'cart_wishlists'

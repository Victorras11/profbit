from django.db import models

# Create your models here.
class Order(models.Model):
    number = models.IntegerField()
    create_date = models.DateTimeField()

class OrderItem(models.Model):
    product_name = models.CharField(max_length = 200)
    product_price = models.IntegerField()
    amount = models.IntegerField()
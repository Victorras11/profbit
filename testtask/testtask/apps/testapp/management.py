from django.template import Context, Template
from testapp.models import Order, OrderItem
from django.utils import timezone
import random

def management(request):
    quantity = request.GET.get('quantity', False)
    i = int(quantity)


    order = random.sample(range(1000, 10000), i)
    name = random.sample(range(1, 100), i)
    price = random.sample(range(100, 9999), i)
    product_amount = [random.randrange(1, 10, 1) for q in range(i)] 


    for c in order:
        a = Order(number = c, create_date = timezone.now())
        a.save()

    for name_data, price_data, amount_data in zip(name, price, product_amount):
        b = OrderItem(product_name = name_data, product_price = price_data, amount = amount_data)
        b.save()


    data = zip(order, name, price, product_amount)

    return data
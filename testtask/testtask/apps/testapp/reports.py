from testapp.models import Order, OrderItem

def report(request):

    data = OrderItem.objects.order_by('-amount')

    return data
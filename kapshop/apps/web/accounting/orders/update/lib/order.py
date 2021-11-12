import json
from django.contrib                                                 import messages
from django.contrib.auth                                            import get_user_model
from django.db.models                                               import Q

from kapshop.apps.db.accounting.orderitems.models                   import OrderItem
from kapshop.apps.db.accounting.orders.models                       import Order
from kapshop.apps.db.products.products.models                       import Product
from kapshop.apps.web.products.products.list.lib.products           import cookieCart

User = get_user_model()


def guestOrder(request, data):

    name = data['form']['name']

    email = data['form']['email']

    cookieData = cookieCart(request)

    items = cookieData['items']

    custom, created = User.objects.get_or_create(email=email)
    custom.username = name
    custom.save()

    order = Order.objects.create(customer= custom, complete=False)

    for item in items:
        product = Product.objects.get(uuid_code=item['product']['uuid_code'])

        orderItem = OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])

    return custom, order
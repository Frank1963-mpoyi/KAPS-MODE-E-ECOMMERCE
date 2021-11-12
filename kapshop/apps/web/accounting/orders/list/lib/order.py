from kapshop.apps.db.accounting.orders.models                               import Order
from kapshop.apps.web.products.products.list.lib.products                   import cookieCart


def  cartData(request):

    if request.user.is_authenticated:

        custom          = request.user

        order, created  = Order.objects.get_or_create(customer=custom, complete=False)

        items           = order.orderitem_set.all()

        cartItems       = order.get_cart_items

    else:

        cookieData      = cookieCart(request)

        cartItems       = cookieData['cartItems']

        order           = cookieData['order']

        items           = cookieData['items']

    return {'cartItems':cartItems, 'order': order, 'items': items}
import json
from django.http                                                    import JsonResponse
from django.contrib                                                 import messages
from django.views.generic                                           import View
from django.contrib.auth                                            import get_user_model

from kapshop.apps.db.products.products.models                       import Product
from kapshop.apps.db.accounting.orders.models                       import Order
from kapshop.apps.db.accounting.orderitems.models                   import OrderItem

User = get_user_model()


class AddToCartAndUpdateItemView(View):

    def post(self, request, **kwargs):

        data        = json.loads(self.request.body)

        productId   = data['productId']

        action      = data['action']

        custom      = request.user

        product     = Product.objects.get(uuid_code=productId)

        order, created      = Order.objects.get_or_create(customer=custom, complete=False)

        orderItem, created  = OrderItem.objects.get_or_create(order=order, product=product)# if it already exist we want to change the value not create a new one

        if action   == 'add':
            orderItem.quantity = (orderItem.quantity +1)
        elif action == 'remove':
            orderItem.quantity -= 1
        elif action == 'delete':
            orderItem.delete()
            messages.success(request, "L'article a bien été supprimé du panier !")

        orderItem.save()

        if  orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)
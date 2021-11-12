import json
from django.http                                                    import JsonResponse
from django.views.generic                                           import View
from django.shortcuts                                               import render, redirect

from kapshop.apps.db.accounting.orders.models                       import Order
from kapshop.apps.db.addresses.models                               import ShippingAddress
from kapshop.apps.web.accounting.orders.list.lib                    import order as order_lib
from kapshop.apps.web.accounting.orders.update.lib                  import order as order_update_lib
from kapshop.common                                                 import user as check_user
from kapshop.common                                                 import kaps_admin as common_kaps_admin
from .input                                                         import input_get_input

class CheckoutView(View):
    template_name = 'apps/accounting/orders/checkout.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff       = check_user.check_allowed_staff(self)

        data        = order_lib.cartData(request)

        kps_admin   = common_kaps_admin.get_kpsadmin(i)

        cartItems   = data['cartItems']
        order       = data['order']
        items       = data['items']

        context = {'i':i, 'items': items, 'order': order, 'cartItems':cartItems, 'staff': staff, 'page_name': 'checkout', 'kps_admin': kps_admin}

        return render(request, self.template_name, context)


class ProcessOrderView(View):

    def post(self, request, **kwargs):

        data = json.loads(self.request.body)

        if request.user.is_authenticated:

            custom          = self.request.user

            order, created  = Order.objects.get_or_create(customer=custom, complete=False)

        else:

            custom, order = order_update_lib.guestOrder(request, data)

        total = (data['form']['total'])  # we need to get form value in body we stringify   body:JSON.stringify({ 'form':userFormData, 'shipping':shippingInfo})
        # print(total)
        if total == float(order.get_cart_total):  # if the front end total == backend total / may be intruder can manipulate the total in front end
            order.complete = True
            if order.complete:
                pass
                #implement email message possible to send the list list of item and amount to the
                # email or implement receipt
        order.save()

        if order.shipping == True:

            ShippingAddress.objects.create(

                customer    = custom,
                order       = order,
                address     = data['shipping']['address'],
                city        = data['shipping']['city'],
                state       = data['shipping']['state'],
                zipcode     = data['shipping']['zipcode'],

            )

        return JsonResponse("Payment submitted....", safe=False)
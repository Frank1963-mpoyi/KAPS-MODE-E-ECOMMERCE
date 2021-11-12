from django.views.generic                                           import View
from django.shortcuts                                               import render, redirect
from django.contrib.auth                                            import get_user_model

from kapshop.apps.web.accounting.orders.list.lib                    import order as order_lib
from kapshop.common                                                 import user as check_user
from kapshop.common                                                 import kaps_admin as common_kaps_admin
from .input import input_get_input

User = get_user_model()


class CartItemView(View):
    template_name = 'apps/accounting/orders/cart.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff       = check_user.check_allowed_staff(self)

        data        = order_lib.cartData(request)

        kps_admin   = common_kaps_admin.get_kpsadmin(i)

        cartItems   = data['cartItems']
        order       = data['order']
        items       = data['items']

        context = {'i':i, 'items': items, 'order': order, 'cartItems':cartItems, 'staff': staff, 'page_name': 'cart', 'kps_admin': kps_admin}

        return render(request, self.template_name, context)
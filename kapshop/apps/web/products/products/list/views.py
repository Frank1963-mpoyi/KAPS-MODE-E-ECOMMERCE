from django.core.paginator                                          import Paginator
from django.views.generic                                           import View
from django.shortcuts                                               import render, redirect
from django.contrib.auth                                            import get_user_model

from kapshop.apps.web.accounting.orders.list.lib                    import order as order_lib
from kapshop.common                                                 import products as common_products
from kapshop.common                                                 import user as check_user
from kapshop.apps.web.home.input                                    import input_get_input

User = get_user_model()


class HomeView(View):
    template_name = 'apps/home/index.html'

    def get(self, request, **kwargs):

        i           = input_get_input(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        staff       = check_user.check_allowed_staff(self)

        data        = order_lib.cartData(request)

        cartItems   = data['cartItems']

        products    = common_products.get_products(i)

        #pagination
        paginator   = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj    = paginator.get_page(page_number)

        context ={'staff' : staff, 'products': page_obj, 'cartItems': cartItems, 'page_name': 'home'}

        return render(request, self.template_name, context)
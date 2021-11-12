from kapshop.common.email                                           import ContactNotificationEmail
from django.contrib                                                 import messages
from django.core.paginator                                          import Paginator
from django.views.generic                                           import View
from django.shortcuts                                               import render, redirect
from django.contrib.auth                                            import get_user_model

from kapshop.apps.web.accounting.orders.list.lib                    import order as order_lib
from kapshop.apps.web.home.forms                                    import ContactForm
from kapshop.common                                                 import products as common_products
from kapshop.common                                                 import user as check_user
from kapshop.common                                                 import kaps_admin as common_kaps_admin
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

        kps_admin   = common_kaps_admin.get_kpsadmin(i)

        #pagination
        paginator   = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj    = paginator.get_page(page_number)

        context ={'staff' : staff, 'products': page_obj, 'cartItems': cartItems, 'page_name': 'home', 'kps_admin': kps_admin}

        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'apps/home/about.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        data = order_lib.cartData(request)

        cartItems = data['cartItems']

        kps_admin = common_kaps_admin.get_kpsadmin(i)

        # TO BE CREATED PLZ
        # our_staffs = Staff.objects.values('id', 'name', 'job_position', 'image').\
        #     order_by('id')

        staff = check_user.check_allowed_staff(self)

        context = {
            'i': i,
            'cartItems' :cartItems ,
            'staff' : staff,
            'page_name' : 'about',
            'kps_admin': kps_admin,
            #'our_staffs' : our_staffs
        }

        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'apps/home/contact.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        staff = check_user.check_allowed_staff(self)

        data =  order_lib.cartData(request)

        kps_admin = common_kaps_admin.get_kpsadmin(i)

        cartItems = data['cartItems']

        form = ContactForm

        # address = get_address(self)

        context = {
            'i': i,
            'page_name': 'contact',
            'staff': staff,
            'cartItems': cartItems,
            'kps_admin': kps_admin,
            # 'address': address,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        form = ContactForm(request.POST or None)


        if form.is_valid():

            ContactForm()

            contactform = ContactForm.objects.create(**form.cleaned_data)# create conrtact model plz

            email = ContactNotificationEmail(contactform)
            email.run()

            message = "Votre formulaire de contact est bien reçu, nous vous envoyons un email de confirmation"
            messages.success(request, message)
            return redirect(self.request.META['HTTP_REFERER'])

        else:
            messages.success(request, " Oops! Vos coordonnées ont échoué, veuillez réessayer !")

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)


class Kaps404View(View):
    template_name = '404.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff = check_user.check_allowed_staff(self)

        kps_admin = common_kaps_admin.get_kpsadmin(i)

        products = common_products.get_products(i)

        data = order_lib.cartData(request)

        cartItems = data['cartItems']

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        context = {
            'i'             : i,
            'page_name'     : '404',
            'staff'         : staff,
            'kps_admin'     : kps_admin,
            'products'      : products,
            'cartItems'     : cartItems,
            # 'country'     : ip_data.get('country'),
        }

        return render(request, self.template_name, context)
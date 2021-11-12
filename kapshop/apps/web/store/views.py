import json
from django.http                                                    import JsonResponse
from django.contrib                                                 import messages
from django.core.paginator                                          import Paginator
from django.views.generic                                           import View
from django.shortcuts                                               import render, redirect
from django.contrib.auth                                            import get_user_model

from kapshop.common.email                                            import ContactNotificationEmail
from kapshop.apps.web.home.forms                                    import GetInTouchForm
from kapshop.apps.web.home.models                                   import Order, Product, OrderItem, ShippingAddress, GetInTouch, Staff
from kapshop.apps.web.home.lib                                      import products as product_lib
from kapshop.common                                                  import user as check_user
from kapshop.apps.web.home.input                                    import input_get_input

User = get_user_model()


class HomeView(View):
    template_name = 'apps/home/index.html'

    def get(self, request, **kwargs):

        i           = input_get_input(self)

        staff       = check_user.check_allowed_staff(self)

        data        = product_lib.carData(request)

        cartItems   = data['cartItems']

        products    = product_lib.get_all_product()
        print(products)

        featured_product    = product_lib.get_top_featured_product()

        best_product        = product_lib.get_best_seller_product()

        # for serach view
        #products    = products.search(query=i['query'])

        #pagination
        paginator   = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj    = paginator.get_page(page_number)

        context = {'products': page_obj, 'cartItems': cartItems, 'featured_product': featured_product,
                   'best_product': best_product, 'staff': staff, 'page_name': 'home'}

        return render(request, self.template_name, context)





class CheckoutView(View):
    template_name = 'apps/home/checkout.html'

    def get(self, request, **kwargs):

        staff       = check_user.check_allowed_staff(self)

        data        = product_lib.carData(request)

        cartItems   = data['cartItems']
        order       = data['order']
        items       = data['items']

        context = {'items': items, 'order': order, 'cartItems':cartItems, 'staff': staff, 'page_name': 'checkout'}

        return render(request, self.template_name, context)



class ProcessOrderView(View):

    def post(self, request, **kwargs):

        data = json.loads(self.request.body)

        if request.user.is_authenticated:

            custom          = self.request.user

            order, created  = Order.objects.get_or_create(customer=custom, complete=False)

        else:

            custom, order = product_lib.guestOrder(request, data)

        total = float(data['form']['total'])  # we need to get form value in body we stringify   body:JSON.stringify({ 'form':userFormData, 'shipping':shippingInfo})

        if total == float(order.get_cart_total):  # if the front end total == backend total / may be intruder can manipulate the total in front end
            order.complete = True
        order.save()

        if order.shipping == True:

            ShippingAddress.objects.create(

                customer    = custom,
                order       = order,
                address     = data['shipping']['addresses'],
                city        = data['shipping']['city'],
                state       = data['shipping']['state'],
                zipcode     = data['shipping']['zipcode'],

            )

        return JsonResponse("Payment submitted....", safe=False)


class ContactView(View):
    template_name = 'apps/home/contact.html'

    def get(self, request, **kwargs):

        staff = check_user.check_allowed_staff(self)

        data        = product_lib.carData(request)

        cartItems   = data['cartItems']

        form        = GetInTouchForm

        #addresses = get_address(self)

        context = {
            'cartItems': cartItems,
            'staff': staff,
            'page_name': 'contact',
            #'addresses': addresses,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        form = GetInTouchForm(request.POST or None)

        if form.is_valid():

            GetInTouchForm()

            contactform = GetInTouch.objects.create(**form.cleaned_data)

            email = ContactNotificationEmail(contactform)
            email.run()

            message = "Votre formulaire de contact est bien reçu, nous vous envoyons un email de confirmation"
            messages.success(request, message)
            return redirect(self.request.META['HTTP_REFERER'])

        else:
            messages.success(request, " Oops! Vos coordonnées ont échoué, veuillez réessayer !")

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'apps/home/about.html'

    def get(self, request, **kwargs):

        data = product_lib.carData(request)

        cartItems = data['cartItems']

        our_staffs = Staff.objects.values('id', 'name', 'job_position', 'image').\
            order_by('id')

        staff = check_user.check_allowed_staff(self)

        context = {
            'cartItems '        :cartItems ,
            'staff'             : staff,
            'page_name'         : 'about',
            'our_staffs'          : our_staffs
        }

        return render(request, self.template_name, context)

def search_view(request):
    template_name= 'search/results-views.html'
    query= request.GET.get('q')

    context ={"query": query}

    if request.GET:
        template_name = 'search/partials/results.html'
        # return render(request, template_name, context)
    return render(request, template_name, context)


class Kaps404View(View):
    template_name = '404.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        # staff = user_common.check_allowed_staff(self)
        #
        # sradmin = sradmin_common.get_sradmin(i)
        #
        # product = product_common.get_first_product(i)
        #
        # login_form    = UserLoginForm
        # register_form = UserRegisterForm

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        context = {
            'i'             : i,
            'page_name'     : '404',
            # 'staff'         : staff,
            # 'sradmin'       : sradmin,
            # 'product'       : product,
            # 'login_form'    : login_form,
            # 'register_form' : register_form,
            # 'country'     : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

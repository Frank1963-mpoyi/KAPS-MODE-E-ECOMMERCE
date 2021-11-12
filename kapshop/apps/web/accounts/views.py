#from threading import Thread

from django.contrib                                     import messages
from django.contrib.auth                                import login, logout
from django.shortcuts                                   import render, redirect
from django.views.generic                               import View

from .forms                                             import UserLoginForm, UserRegisterForm
from .input                                             import input_post_input
from kapshop.apps.web.accounting.orders.list.lib                    import order as order_lib


class UserRegisterView(View):
    template_name = 'apps/accounts/register.html'

    def get(self, request, **kwargs):
        data = order_lib.cartData(request)

        cartItems = data['cartItems']

        register_form = UserRegisterForm

        context = {
            'cartItems ': cartItems,
            'page_name': 'home',
            'register_form': register_form,
        }

        return render(self.request, self.template_name, context)

    def post(self, request, **kwargs):

        i = input_post_input(self)

        register_form = UserRegisterForm(request.POST or None)

        if register_form.is_valid():
            kaps_user = register_form.save(commit=False)

            kaps_user.username  = kaps_user.email
            kaps_user.is_active = True
            kaps_user.last_updated_by = kaps_user.username

            kaps_user.save()

            messages.success(request, "Vous avez créé votre compte avec succès.")

            return redirect("web:accounts:login")

        messages.warning(request, "Vous ne vous êtes pas inscrit, veuillez réessayer.")

        context = {
            'i'             : i,
            'register_form' : register_form,
        }

        return render(self.request, self.template_name, context)


class UserLoginView(View):
    template_name = 'apps/accounts/login.html'

    def get(self, request, **kwargs):

        login_form = UserLoginForm

        data = order_lib.cartData(request)

        cartItems = data['cartItems']

        context = {
            'login'     : 'login',
            'login_form'    : login_form,
            'cartItems ': cartItems,
        }

        return render(self.request, self.template_name, context)

    def post(self, request, **kwargs):

        data = order_lib.cartData(request)

        cartItems = data['cartItems']

        form = UserLoginForm(request.POST or None)

        if form.is_valid():

            user_obj = form.cleaned_data.get('user_obj')

            login(request, user_obj)

            messages.success(request, f"Bienvenue! {(user_obj.fullname).title()}, à KAPS MODE.")
            return redirect('web:home:home')

        messages.warning(request, "Vous n'êtes pas connecté, veuillez vérifier vos informations d'identification.")

        context ={'login_form': form,
                  'cartItems': cartItems
                  }
        return render(self.request, self.template_name, context)


class UserLogoutView(View):
    template_name = 'apps/home/index.html'

    def get(self, request, **kwargs):

        logout(request)

        messages.info(request, f" Vous êtes déconnecté. Bonne journée !.")

        return redirect('web:home:home')
from django.contrib                                 import messages
from django.contrib.auth.mixins                     import LoginRequiredMixin
from django.shortcuts                               import render, redirect
from django.views                                   import View

from kapshop.common                                  import user     as user_common
from kapshop.core.user_level_mixins                  import UserLevelMixin
from .forms                                         import  KpsAdminCreateForm
from .input                                         import input_post_input, input_get_input
from .lib                                           import kaps_admin  as kpsadmin_lib


# Create your views here.
class KapsAdminCreateView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/dashboard/kaps_admin.html', 'KPS-MNG-3'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff    = user_common.check_allowed_staff(self)

        kpsadmin = kpsadmin_lib.get_kapsadmin(i)

        info_form = KpsAdminCreateForm(instance = kpsadmin, staff = staff)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        form = KpsAdminCreateForm

        context = {
            'i'         : i,
            'page_name' : 'kps_admins',
            'menu'      : 'Administration',
            'staff'     : staff,
            'kpsadmin'  : kpsadmin,
            'info_form' : info_form,
            # 'country' : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        i = input_post_input(self)

        staff  = user_common.check_allowed_staff(self)

        kpsadmin = kpsadmin_lib.get_kapsadmin(i)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        form    =  KpsAdminCreateForm(request.POST or None, instance=kpsadmin, staff=staff)

        message = "Désolé, une erreur s'est produite. Details non créés."

        print(form.errors)

        if form.is_valid():

            kpsadmin = kpsadmin_lib.create_kapsadmin(i, staff)

            message = f"Details '{kpsadmin.code}' créés avec succès."

            if not kpsadmin:
                message = "Veuillez vérifier tous les champs du formulaire et réessayer."

        print(message)
        messages.success(request, message)

        return redirect('web:sr_admins:list')

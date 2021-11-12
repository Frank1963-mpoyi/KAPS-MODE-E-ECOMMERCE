from django.contrib.auth.mixins                             import LoginRequiredMixin
from django.shortcuts                                       import render
from django.views.generic                                   import View

from kapshop.common                                         import user    as user_common
from ..create.forms                                         import  KpsAdminCreateForm
from kapshop.core.user_level_mixins                         import UserLevelMixin
from .input                                                 import input_get_input
from .lib                                                   import kaps_admin as kpsdmin_lib


# Create your views here.
class KapsAdminListView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/dashboard/kaps_admin.html', 'KPS-MNG-3'

    def get(self, request, **kwargs):
        i = input_get_input(self)

        staff = user_common.check_allowed_staff(self)

        kpsadmin = kpsdmin_lib.get_kpsadmin(i)

        info_form = KpsAdminCreateForm(instance= kpsadmin, staff=staff)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        context = {
            'i': i,
            'page_name': 'sr_admins',
            'menu': 'Administration',
            'staff': staff,
            'kpsadmin': kpsadmin,
            'info_form': info_form,
            # 'country'     : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

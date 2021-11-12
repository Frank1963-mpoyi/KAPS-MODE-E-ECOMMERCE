from django.contrib.auth.mixins                     import LoginRequiredMixin
from django.shortcuts                               import render
from django.views                                   import View

from kapshop.common                                  import user as user_common
from kapshop.core.user_level_mixins                  import UserLevelMixin

from kapshop.apps.web.dashboard.input import input_get_input


# Create your views here.
class DashboardView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/dashboard/index.html', 'KPS-MNG-3'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff  = user_common.check_allowed_staff(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        context = {
            'i'             : i,
            'page_name'     : 'dashboard',
            'menu'          : 'Dashboard',
            'staff'         : staff,
            # 'country'       : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

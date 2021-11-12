from django.urls                                                    import path

from kapshop.apps.web.kaps_admins.create.views                     import KapsAdminCreateView
from kapshop.apps.web.kaps_admins.list.views                       import KapsAdminListView


app_name = 'kaps_admins'

urlpatterns = [

    path('create/',                KapsAdminCreateView.as_view(),                name='create'),
    # path('delete/<code>',           ProductDeleteteView.as_view(),              name='delete'),
    path('list/',                   KapsAdminListView.as_view(),                  name='list'),
    # path('update/<code>',           ProductUpdateView.as_view(),                name='update'),

]

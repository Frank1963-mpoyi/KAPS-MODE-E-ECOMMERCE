from django.urls                                        import path, include

app_name = "web"


urlpatterns = [
    path('',                                        include('kapshop.apps.web.home.urls')),
    path('accounting/',                             include('kapshop.apps.web.accounting.urls')),
    path('products/',                               include('kapshop.apps.web.products.urls')),
    path('accounts/',                               include('kapshop.apps.web.accounts.urls')),
    path('addresses/',                              include('kapshop.apps.web.addresses.urls')),
    path('dashboard/',                              include('kapshop.apps.web.dashboard.urls')),
    path('kaps_admins/',                            include('kapshop.apps.web.kaps_admins.urls')),
]
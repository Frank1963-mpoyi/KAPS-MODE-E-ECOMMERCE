from django.urls                                        import path, include

app_name = "accounting"

urlpatterns = [
    # path('banks/',                                include('kapshop.apps.web.accounting.bank.urls')),
    # path('coupons/',                              include('kapshop.apps.web.accounting.coupons.urls')),
    # path('orderitems/',                           include('kapshop.apps.web.accounting.orderitems.urls')),
    path('orders/',                                 include('kapshop.apps.web.accounting.orders.urls')),
]
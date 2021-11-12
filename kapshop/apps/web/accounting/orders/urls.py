from django.urls                                                    import path

from kapshop.apps.web.accounting.orders.list.views                  import CartItemView
from kapshop.apps.web.accounting.orderitems.create.views            import AddToCartAndUpdateItemView
from kapshop.apps.web.accounting.orders.update.views                import CheckoutView, ProcessOrderView

app_name = "orders"

urlpatterns = [
    path('cart/',                                   CartItemView.as_view(),                     name="cart"),
    path('update/',                                 AddToCartAndUpdateItemView.as_view(),       name="update"),
    path('checkout/',                               CheckoutView.as_view(),                     name="checkout"),
    path('process_order/',                          ProcessOrderView.as_view(),                 name="process_order"),
]
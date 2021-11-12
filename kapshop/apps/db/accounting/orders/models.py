import uuid
from django.db                                                          import models
from django.contrib.auth                                                import get_user_model

from kapshop.common.global_choices                                      import ORDER_TYPE, PAYMENT_TYPE
from kapshop.core.model_mixins                                          import AuditFields, OrdersDetailFields
from kapshop.core.utils                                                 import order_randcode_gen, transaction_id_randcode_gen

User = get_user_model()


class Order(AuditFields, OrdersDetailFields):

    uuid_code                   = models.UUIDField('ID',                primary_key=True,   default=uuid.uuid4,     editable=False, null=False)
    code                        = models.CharField('CODE',              max_length=100,     blank=False,            default=order_randcode_gen)
    transaction_id              = models.CharField('TRANSACTION ID',    max_length=120,     blank=True,             default=transaction_id_randcode_gen)

    complete                    = models.BooleanField('COMPLETE',       default=False)

    customer                    = models.ForeignKey(User,                   on_delete=models.CASCADE,       null=True,                          blank=False)
    billing_address             = models.ForeignKey('addresses.Address',    on_delete=models.SET_NULL,      related_name='billing_address',     null=True, blank=False)
    shipping_address            = models.ForeignKey('addresses.Address',    on_delete=models.SET_NULL,      related_name='shipping_address',    null=True, blank=False)
    coupon                      = models.ForeignKey('coupons.Coupon',       on_delete=models.PROTECT,       related_name='orders',              null=True, blank=False)
    location                    = models.ForeignKey('locations.Location',   on_delete=models.PROTECT,       related_name='orders',              null=True, blank=False)

    payment                     = models.ForeignKey('payments.Payment',        on_delete=models.PROTECT,    related_name='orders',              null=True, blank=False)
    being_delivered             = models.CharField(max_length=120, blank=True, null=True)
    received                    = models.CharField(max_length=120, blank=True, null=True)
    refund_requested            = models.CharField(max_length=120, blank=True, null=True)
    refund_granted              = models.CharField(max_length=120, blank=True, null=True)
    order_type                  = models.CharField('ORDER TYPE', choices=ORDER_TYPE,        max_length=2,   null=True, blank=False)
    payment_type                = models.CharField('PAYMENT TYPE', choices=PAYMENT_TYPE,    max_length=2,   null=True, blank=False)

    class Meta:

        app_label   = 'orders'
        db_table    = 'Order'
        verbose_name_plural = 'orders'

    # def __str__(self):
    #     return self.user.username

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])

        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()

        for i in orderitems:
            if i.product.digital == False:
                shipping = True

        return shipping
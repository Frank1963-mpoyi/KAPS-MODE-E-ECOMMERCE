import uuid
from django.db.models.signals                                       import pre_save
from django.db                                                      import models
from django.contrib.auth                                            import get_user_model
from django.core.validators                                         import MinValueValidator, MaxValueValidator
from kapshop.common.upload_images                                    import upload_img_path
from kapshop.common.global_choices                                   import LABEL_CHOICES, BADGE_NEWS
from kapshop.common.search                                           import ProductsManager
from kapshop.core.model_mixins                                       import AuditFields, EmailFields
from kapshop.core.utils                                              import unique_slug_generator, product_randcode_gen, order_randcode_gen, orderitem_randcode_gen, \
                                                                            shipping_randcode_gen, transaction_id_randcode_gen, get_in_touch_randcode_gen

User = get_user_model()


class OrderItem(AuditFields):

    uuid_code                       = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False, null=False)
    code                            = models.CharField('CODE', max_length=100, blank=False, default=orderitem_randcode_gen)

    customer                        = models.ForeignKey(User,             verbose_name="USER",    on_delete=models.CASCADE, null=True, blank=True)
    product                         = models.ForeignKey('products.Product',          verbose_name="PRODUCT", on_delete=models.CASCADE)
    order                           = models.ForeignKey('orders.Order',            verbose_name="ORDER",   on_delete=models.CASCADE)
    #location                        = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='items',     null=True)

    complete                        = models.BooleanField(default=False)
    quantity                        = models.PositiveSmallIntegerField('QUANTITY',
                                                validators=[MinValueValidator(1), MaxValueValidator(999)], default=0,
                                                blank=True, null=True)
    item_itno                       = models.PositiveSmallIntegerField('ITEM NUMBER IN ORDER',
                                                 validators=[MinValueValidator(1), MaxValueValidator(999)], default=1,
                                                 blank=True, null=True)

    price_buy                       = models.DecimalField('PRICE BUY',              max_digits=19, default=0, decimal_places=2, blank=True)
    price_buy_original              = models.DecimalField('PRICE BUY ORIGINAL',     max_digits=19, default=0, decimal_places=2, blank=True)
    price_sell                      = models.DecimalField('PRICE SELL',             max_digits=19, default=0, decimal_places=2, blank=True)
    price_sell_original             = models.DecimalField('PRICE SELL ORIGINAL',    max_digits=19, default=0, decimal_places=2, blank=True)

    bool_active                     = models.BooleanField('IS ACTIVE', default=True)

    class Meta:

        app_label   = 'orderitems'
        db_table    = 'OrderItem'
        verbose_name_plural = 'orderitems'

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    @property
    def get_total(self):
        total = self.product.price * self.quantity

        return total

    @property
    def get_total_discount_price(self):
        total = self.product.discount_price * self.quantity

        return total

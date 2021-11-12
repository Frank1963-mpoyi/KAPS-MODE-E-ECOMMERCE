import uuid

from django.contrib.auth                                        import get_user_model
from django.conf                                                import settings
from django.db                                                  import models

from django_countries.fields                                    import CountryField

from kapshop.common.global_choices                               import ADDRESS_CHOICES
from kapshop.core.model_mixins                                   import AuditFields
from kapshop.core.utils                                          import randcode_gen, shipping_randcode_gen

User = get_user_model()

# Create your models here.
class Address(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4,       editable=False,           null=False)

    customer            = models.ForeignKey(User, on_delete=models.PROTECT, related_name='addresses')
    location            = models.ForeignKey('locations.Location', on_delete=models.PROTECT, related_name='addresses',   null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=randcode_gen)

    street_address      = models.CharField('STREET NAME',           max_length=100,     blank=True,                     null=True)
    apartment_address   = models.CharField('HOME NUMBER',           max_length=100,     blank=True,                     null=True)
    country             = CountryField('COUNTRY CODE',              multiple=False,     blank=True,                     null=True)
    zipcode             = models.CharField('POSTAL',                max_length=100,     blank=True,                     null=True)
    address_type        = models.CharField('ADDRESS TYPE',          max_length=1, choices=ADDRESS_CHOICES, blank=True,  null=True)
    payment_option      = models.CharField('PAYMENT OPTION',        max_length=100,     blank=True,                     null=True)

    default             = models.BooleanField('DEFAULT ADDRESS',    default=False,      blank=True,                     null=True)

    class Meta:
        app_label   = 'addresses'
        db_table    = 'addresses'
        verbose_name_plural = 'addresses'


class ShippingAddress(AuditFields):

    code                                = models.CharField('CODE', max_length=100, blank=False, default=shipping_randcode_gen)

    customer                            = models.ForeignKey(User,       verbose_name="USER", on_delete=models.CASCADE)
    order                               = models.ForeignKey('orders.Order',          verbose_name="ORDER", on_delete=models.CASCADE)
    address                             = models.CharField("ADDRESS",       max_length=250, null=True, blank=True)
    city                                = models.CharField("CITY",          max_length=250, null=True, blank=True)
    state                               = models.CharField("STATE",         max_length=250, null=True, blank=True)
    zipcode                             = models.CharField("ZIP CODE",      max_length=250, null=True, blank=True)
    date_added                          = models.DateTimeField("DATE TIME", auto_now_add=True)

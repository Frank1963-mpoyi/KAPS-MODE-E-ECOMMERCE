import uuid
from django.db.models.signals                                       import pre_save
from django.db                                                      import models
from django.contrib.auth                                            import get_user_model

from kapshop.common.upload_images                                    import upload_img_path
from kapshop.common.global_choices                                   import LABEL_CHOICES, BADGE_NEWS
from kapshop.common.search                                           import ProductsManager
from kapshop.core.model_mixins                                       import AuditFields, EmailFields, ProductStockFields, ProductCategoryFields
from kapshop.core.utils                                              import unique_slug_generator, product_randcode_gen, order_randcode_gen, orderitem_randcode_gen, \
                                                                            shipping_randcode_gen, transaction_id_randcode_gen, get_in_touch_randcode_gen

User = get_user_model()


class Product(AuditFields ,ProductStockFields, ProductCategoryFields):
    uuid_code               = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False, null=False)
    code                    = models.CharField('CODE',      max_length=100,     blank=False, default=product_randcode_gen)
    slug                    = models.SlugField('SLUG',      unique=True, blank=True, null=True)

    category                = models.ForeignKey('categories.Category',      on_delete=models.PROTECT, related_name='products_categories', blank=True,  null=True)
    subcategory             = models.ForeignKey('categories.Category',      on_delete=models.PROTECT, related_name='products_subcategories', null=True, blank=True)
    color                   = models.ForeignKey('colors.Color',             on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    store                   = models.ForeignKey('stores.Store',             on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    size                    = models.ForeignKey('sizes.Size',               on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    title                   = models.CharField('TITLE' ,                    max_length=120)


    image                   = models.ImageField('IMAGE',     upload_to=upload_img_path, blank=True, null=True)
    price                   = models.DecimalField('PRICE',              max_digits=19,      default=0,              decimal_places=2,  blank=True)

    discount_price          = models.DecimalField('DISCOUNTED PRICE',   max_digits=19,      default=0,              decimal_places=2,  blank=True)

    description             = models.CharField('DESCRIPTION',           max_length=250, blank=True, null=True)

    label                   = models.CharField('LABEL',                 max_length=50,     choices=LABEL_CHOICES,  blank=True,  null=True)
    badge                   = models.CharField('BADGE NEWS',            max_length=250, choices=BADGE_NEWS, blank=True, null=True)

    digital                 = models.BooleanField("DIGITAL",            default=False, blank=True, null=True)
    top_featured            = models.BooleanField("TOP FEATURE",        default=False,      blank=True, null=True)
    best_seller             = models.BooleanField("BEST SELLER",        default=False,      blank=True, null=True)

    objects                 = ProductsManager()

    class Meta:

        app_label   = 'products'
        db_table    = 'Product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# class GetInTouch(EmailFields):
#
#     code                                = models.CharField('CODE', max_length=100, blank=False, default=get_in_touch_randcode_gen)
#
#     fullname                            = models.CharField(max_length=120)
#     subject                             = models.CharField(max_length=250)
#     message                             = models.TextField()
#
#     def __str__(self):
#         return self.fullname


# class Staff(models.Model):
#     code                                = models.CharField('CODE',      max_length=100,     blank=False, default=product_randcode_gen)
#
#     name                                = models.CharField(max_length=250)
#     job_position                        = models.CharField(max_length=250)
#     image                               = models.ImageField('IMAGE', upload_to=upload_img_path, blank=True, null=True)
#
#     def __str__(self):
#         return self.name

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)
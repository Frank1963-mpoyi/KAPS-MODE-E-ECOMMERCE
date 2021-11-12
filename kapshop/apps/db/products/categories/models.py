import uuid

from django.db                                                  import models

from kapshop.core.model_mixins                                   import AuditFields, ProductCategoryFields
from kapshop.core.utils                                          import categ_randcode_gen


# Create your models here.
class Category(AuditFields, ProductCategoryFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    category            = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='categories', null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=categ_randcode_gen)

    title               = models.CharField('TITLE',                 max_length=100,     blank=True,                     null=True)
    description         = models.TextField('DESCRIPTION',                               blank=True,                     null=True)

    sub                 = models.BooleanField('SUB-CATEGORY',       default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label   = 'categories'
        db_table    = 'categories'
        verbose_name_plural = 'categories'

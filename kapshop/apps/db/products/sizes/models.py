import uuid

from django.db                                                  import models

from kapshop.core.model_mixins                                   import AuditFields
from kapshop.core.utils                                          import size_randcode_gen


# Create your models here.
class Size(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=size_randcode_gen)

    title               = models.CharField('TITLE',                 max_length=250,     blank=True,                     null=True)
    size_number         = models.PositiveSmallIntegerField('NUMBER',                    blank=True,                     null=True)
    size_symbol         = models.CharField('SYMBOL',                max_length=5,       blank=True,                     null=True)
    country_orig        = models.CharField('ORIGIN COUNTRY',        max_length=5,       blank=True,                     null=True)
    description         = models.TextField('DESCRIPTION',                               blank=True,                     null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label   = 'sizes'
        db_table    = 'sizes'
        verbose_name_plural = 'sizes'

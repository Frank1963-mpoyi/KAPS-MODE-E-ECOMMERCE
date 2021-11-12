import uuid

from django.db                                                  import models

from kapshop.core.model_mixins                                   import AuditFields
from kapshop.core.utils                                          import color_randcode_gen


# Create your models here.
class Color(AuditFields):

    uuid_code   = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    color       = models.ForeignKey('colors.Color', on_delete=models.PROTECT, related_name='colors', null=True)

    token_key   = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code        = models.CharField('CODE',                  max_length=100,     blank=False, default=color_randcode_gen)

    title       = models.CharField('TITLE',                 max_length=250,     blank=True,                     null=True)
    shade       = models.CharField('SHADE',                 max_length=250,     blank=True,                     null=True)
    description = models.TextField('DESCRIPTION',                               blank=True,                     null=True)
    bool_shade  = models.BooleanField('IS SHADE',           default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label   = 'colors'
        db_table    = 'colors'
        verbose_name_plural = 'colors'

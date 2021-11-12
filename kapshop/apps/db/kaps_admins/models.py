import uuid

from django.db                                  import models

from kapshop.core.model_mixins                   import AuditFields, AddressFields, EmailFields, PhoneFields
from kapshop.core.utils                          import randcode_gen


# Create your models here.
class KapsAdmin(AuditFields, AddressFields, EmailFields, PhoneFields):

    uuid_code   = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4,       editable=False,       null=False)

    location    = models.ForeignKey('locations.Location', on_delete=models.PROTECT, related_name='admins',  null=True, blank=True)

    token_key   = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True, null=True)
    code        = models.CharField('CODE',                  max_length=100,     blank=False, default=randcode_gen)

    bool_active = models.BooleanField('IS ACTIVE',    default=False,      blank=True,                       null=True)

    class Meta:
        app_label   = 'kaps_admins'
        db_table    = 'kps_admins'
        verbose_name_plural = 'kps_admins'

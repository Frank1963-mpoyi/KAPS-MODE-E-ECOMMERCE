from django.db.models                                   import Q

from kapshop.apps.db.kaps_admins.models                     import KapsAdmin
from kapshop.common                                         import country as country_common



def get_kpsadmin(i):

    kpsadmin = KapsAdmin.objects \
        .exclude(
            Q(bool_active  = False) |
            Q(bool_deleted = True)
        ) \
        .values(
            'uuid_code', 'token_key', 'code', 'bool_active', 'street_name', 'house_number', 'post_code', 'area', 'city',
            'region', 'country', 'email1', 'email2', 'email3', 'email4', 'phone1', 'phone2', 'phone3',
            'phone4', 'datetime_created', 'datetime_updated', 'last_updated_by', 'bool_deleted'
        ).first()

    if kpsadmin:
        pays = country_common.get_countries_translated(i)

        kpsadmin['country'] = pays[kpsadmin['country']]
        if kpsadmin['post_code'] == 0 or kpsadmin['post_code'] == '0':
            kpsadmin['post_code'] = None

    return kpsadmin
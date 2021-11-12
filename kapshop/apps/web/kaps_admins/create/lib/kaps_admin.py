from django.db.models                                               import Q

from kapshop.apps.db.kaps_admins.models                             import KapsAdmin
from kapshop.common                                                 import country as country_common


def get_kapsadmin(i):
    kapsadmin = KapsAdmin.objects \
        .exclude(
        Q(bool_active=False) |
        Q(bool_deleted=True)
    ) \
        .values(
        'uuid_code', 'token_key', 'code', 'bool_active', 'street_name', 'house_number', 'post_code', 'area', 'city',
        'region', 'country', 'email1', 'email2', 'email3', 'email4', 'phone1', 'phone2', 'phone3',
        'phone4', 'datetime_created', 'datetime_updated', 'last_updated_by', 'bool_deleted'
    ).first()

    if kapsadmin:
        pays = country_common.get_countries_translated(i)

        kapsadmin['country'] = pays[kapsadmin['country']]
        if kapsadmin['post_code'] == 0 or kapsadmin['post_code'] == '0':
            kapsadmin['post_code'] = None

    return kapsadmin


def create_kapsadmin(i, staff):

    if staff['management']:

        kapsadmin = KapsAdmin.objects \
            .create(
            # name            = i['name'],
            email1=i['email1'],
            email2=i['email2'],
            email3=i['email3'],
            email4=i['email4'],
            phone1=i['phone1'],
            phone2=i['phone2'],
            phone3=i['phone3'],
            phone4=i['phone4'],
            street_name=i['street_name'],
            house_number=i['house_number'],
            post_code=i['post_code'],
            area=i['area'],
            city=i['city'],
            region=i['region'],
            country=i['country'],
            bool_active=True,
            last_updated_by=i['user_fullname'],
        )

        return kapsadmin

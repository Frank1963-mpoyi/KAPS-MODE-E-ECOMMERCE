def input_get_input(self):
    _i = self.request.GET
    user = self.request.user

    i = {
        'user': user,
        'user_fullname': user.fullname,

        'name': _i.get('iname'),
        'email1': _i.get('iemail1'),
        'email2': _i.get('iemail2'),
        'email3': _i.get('iemail3'),
        'email4': _i.get('iemail4'),
        'phone1': _i.get('iphone1'),
        'phone2': _i.get('iphone2'),
        'phone3': _i.get('iphone3'),
        'phone4': _i.get('iphone4'),
        'street_name': _i.get('istreet_name'),
        'house_number': _i.get('ihouse_number'),
        'post_code': _i.get('ipost_code'),
        'area': _i.get('iarea'),
        'city': _i.get('icity'),
        'region': _i.get('iregion'),
        'country': _i.get('icountry'),
        'active': _i.get('iactive'),
    }

    return i

def input_get_input(self):
    _i = self.request.GET

    i = {
        'user': self.request.user,
    }

    return i


def input_post_input(self):
    _i = self.request.POST

    i = {
        'user'      : self.request.user,

        "fullname"  : _i.get("fullname", ''),
        "phone"     : _i.get("phone", ''),
        "email"     : _i.get("email", ''),
        "subject"   : _i.get("subject", ''),
        "message"   : _i.get("message", ''),

    }

    return i


def input_get_input(self):

    _i   = self.request.GET
    _k   = self.kwargs
    #user = self.request.user

    i = {
        # 'user'          : user,
        # 'user_fullname' : user.fullname,
        #'code_user_id'  : user.uuid_code,

        'type'          : _i.get('type'),
        'assignee'      : _i.get('assignee'),
        'assigner'      : _i.get('assigner'),

        'code'          : _k.get('code'),
    }

    return i

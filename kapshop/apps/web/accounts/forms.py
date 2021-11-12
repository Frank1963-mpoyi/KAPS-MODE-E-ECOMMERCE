from django                                             import forms
from django.contrib.auth                                import get_user_model
from django.db.models                                   import Q

User = get_user_model()


class UserRegisterForm(forms.ModelForm):

    fullname    = forms.CharField(label='', widget=forms.TextInput(attrs={"title" : "Full name ", "class":"form-control", "id":"fullname"}),required=False)
    email       = forms.CharField(label='', widget=forms.EmailInput(attrs={"title" : "E-mail Adress", "class":"form-control", "id":"emailAddress"}),required=False)
    password    = forms.CharField(label='', widget=forms.PasswordInput(attrs={"title" : "password", "class":"form-control",  "id":"myInput"}),required=False)
    password1   = forms.CharField(label='', widget=forms.PasswordInput(attrs={"title" : "Confirm Password ", "class":"form-control", "id":"myInput"}),required=False)

    class Meta:
        model   = User
        fields  = [
            'fullname',
            'email',
            # 'username',
        ]

    def clean(self):

        fullname        = self.cleaned_data.get('fullname')
        email           = self.cleaned_data.get('email')
        password        = self.cleaned_data.get('password')
        password1       = self.cleaned_data.get('password1')

        if not fullname:
            self.add_error('fullname', "Veuillez mettre votre nom complet")

        if not email:
            self.add_error('email', "Veuillez mettre votre e-mail")

        if not password:
            self.add_error('password', "Veuillez mettre votre mot de passe")

        if password and password1 and password != password1:
            self.add_error('password1', "votre mot de passe ne correspond pas.")

        user = User.objects \
            .filter(
                Q(username__iexact  = email) |
                Q(email__iexact     = email)
            ) \
            .exclude(
                # Q(is_active    = False) |
                Q(bool_deleted = True)
            )

        if user:
            raise forms.ValidationError("Ce compte a été utilisé, veuillez en prendre un autre.")

        return self.cleaned_data

    def save(self, commit=True):

        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user


class UserLoginForm(forms.Form):

    email    = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={"title" : "email adress", "class":"form-control","id":"emailAddress", "placeholder":"" }), required=False)
    password = forms.CharField(label='Mot de pass', widget=forms.PasswordInput(attrs={"title" : "password","class":"form-control",  "id":"myInput" , "placeholder":""}), required=False)

    def clean(self, *args, **kwargs):

        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        username_or_email_final = User.objects \
            .filter(
                Q(username__iexact  = email) |
                Q(email__iexact     = email)
            ) \
            .exclude(
                # Q(is_active     = False) |
                Q(bool_deleted  = True)
            ) \
            .distinct()

        if not email:
            self.add_error('email', "Veuillez mettre votre adresse e-mail")

        if not password:
            self.add_error('password', "Veuillez mettre votre mot de passe ")

        if not username_or_email_final.exists() and username_or_email_final != 1:
            raise forms.ValidationError("Vous n'avez pas de compte chez nous, vous devez vous inscrire ")

        user_obj = username_or_email_final.first()

        if not user_obj.check_password(password):
            raise forms.ValidationError("vos informations ne sont pas correctes veuillez réessayer !")

        self.cleaned_data['user_obj'] = user_obj

        return self.cleaned_data
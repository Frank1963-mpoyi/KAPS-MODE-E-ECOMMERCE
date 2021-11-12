from crispy_forms.helper                                import FormHelper

from django                                             import forms

from kapshop.common                                      import country as country_common


COUNTRIES_CHOICES = country_common.get_countries_choices_translated('FR')

class KpsAdminCreateForm(forms.Form):

    # iname           = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title" : "Le Nom de la Boutique", "placeholder": "Le Nom de la Boutique"}), required=True)
    iemail1         = forms.CharField(label='', widget=forms.EmailInput(attrs={"class": "form-control", "title" : "L'e-mail principal", "placeholder": "L'e-mail principal"}), required=True)
    iemail2         = forms.CharField(label='', widget=forms.EmailInput(attrs={"class": "form-control", "title" : "L'e-mail secondaire", "placeholder": "L'e-mail secondaire"}), required=False)
    iemail3         = forms.CharField(label='', widget=forms.EmailInput(attrs={"class": "form-control", "title" : "L'e-mail tertiaire", "placeholder": "L'e-mail tertiaire"}), required=False)
    iemail4         = forms.CharField(label='', widget=forms.EmailInput(attrs={"class": "form-control", "title" : "L'e-mail quaternaire", "placeholder": "L'e-mail quaternaire"}), required=False)
    iphone1         = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "Le numéro principal", "placeholder": "Le numéro principal"}), required=True)
    iphone2         = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title" : "Le numéro secondaire", "placeholder": "Le numéro secondaire"}), required=False)
    iphone3         = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title" : "Le numéro tertiaire", "placeholder": "Le numéro tertiaire"}), required=False)
    iphone4         = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title" : "Le numéro quaternaire", "placeholder": "Le numéro quaternaire"}), required=False)
    istreet_name    = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "La Rue ou L'avenue", "placeholder": "Av, Limete"}), required=True)
    ihouse_number   = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "Le Numero", "placeholder": "12"}), required=False)
    ipost_code      = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "Le Code Postal", "placeholder": "7460"}), required=False)
    iarea           = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "La Commune", "placeholder": "La Commune"}), required=True)
    icity           = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "La Ville", "placeholder": "Kinshasa"}), required=True)
    iregion         = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "title": "La Province", "placeholder": "Kinshasa"}), required=True)
    icountry        = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control'}), initial='CD', choices=COUNTRIES_CHOICES, required=True)
    ibool_active    = forms.BooleanField(label='', widget=forms.CheckboxInput(attrs={"title": "Est-il actif?"}), required=False)

    def __init__(self, *args, **kwargs):
        staff   = kwargs.pop('staff')
        kapsadmin = kwargs.pop('instance')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        if kapsadmin:
            # self.fields['iname'].initial            = kapsadmin['name'] if kapsadmin['name'] else 'KAPS MODE'
            self.fields['iemail1'].initial          = kapsadmin['email1'] if kapsadmin['email1'] else None
            self.fields['iemail2'].initial          = kapsadmin['email2'] if kapsadmin['email2'] else None
            self.fields['iemail3'].initial          = kapsadmin['email3'] if kapsadmin['email3'] else None
            self.fields['iemail4'].initial          = kapsadmin['email4'] if kapsadmin['email4'] else None
            self.fields['iphone1'].initial          = kapsadmin['phone1'] if kapsadmin['phone1'] else None
            self.fields['iphone2'].initial          = kapsadmin['phone2'] if kapsadmin['phone2'] else None
            self.fields['iphone3'].initial          = kapsadmin['phone3'] if kapsadmin['phone3'] else None
            self.fields['iphone4'].initial          = kapsadmin['phone4'] if kapsadmin['phone4'] else None
            self.fields['istreet_name'].initial     = kapsadmin['street_name'] if kapsadmin['street_name'] else None
            self.fields['ihouse_number'].initial    = kapsadmin['house_number'] if kapsadmin['house_number'] else None
            self.fields['ipost_code'].initial       = kapsadmin['post_code'] if kapsadmin['post_code'] else 0
            self.fields['iarea'].initial            = kapsadmin['area'] if kapsadmin['area'] else 'Gombe'
            self.fields['icity'].initial            = kapsadmin['city'] if kapsadmin['city'] else 'Kinshasa'
            self.fields['iregion'].initial          = kapsadmin['region'] if kapsadmin['region'] else 'Kinshasa'
            # self.fields['icountry'].initial         = kapsadmin['country'] if kapsadmin['country'] else
        else:
            # self.fields['iname'].initial        = 'KAPS MODE'
            self.fields['ipost_code'].initial   = 0
            self.fields['iarea'].initial        = 'Gombe'
            self.fields['icity'].initial        = 'Kinshasa'
            self.fields['iregion'].initial      = 'Kinshasa'

        self.fields['ibool_active'].initial     = True
        self.fields['ibool_active'].widget.attrs['readonly'] = True
        self.fields['ibool_active'].widget.attrs['disabled'] = True

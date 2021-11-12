from crispy_forms.helper                                import FormHelper
from dal                                                import autocomplete

from django                                             import forms

from kapshop.common.global_choices                       import LABEL_CHOICES
from kapshop.apps.db.products.categories.models          import Category
from kapshop.apps.db.products.colors.models              import Color
from kapshop.apps.db.products.sizes.models               import Size


class ProductCreateForm(forms.Form):

    ititle          = forms.CharField(label='',     widget=forms.TextInput(attrs={"class":"form-control","title" : "Le Titre du Produit", "placeholder": "Le Titre du Produit"}), required=True)
    islug           = forms.CharField(label='',     widget=forms.TextInput(attrs={"class":"form-control","title" : "Le Nom du Produit", "placeholder": "Le Nom du Produit"}), required=False)
    iimage          = forms.ImageField(label='',    required=False)
    idescription    = forms.CharField(label='',     widget=forms.Textarea(attrs={"class":"form-control","rows" : "4", "title" : "La Description", "placeholder": "La Description"}),required=True)
    iprice          = forms.CharField(label='',     widget=forms.TextInput(attrs={"class":"form-control","title" : "Le Prix", "placeholder": "80.00"}), required=False)
    idiscount_price = forms.CharField(label='',     widget=forms.TextInput(attrs={"class":"form-control","title" : "Le Prix de la reduction", "placeholder": "72.50"}), required=False)
    iqty_stock      = forms.CharField(label='',     widget=forms.TextInput(attrs={"class":"form-control","title" : "La Quantite", "placeholder": "50"}), required=False)
    ilabel          = forms.ChoiceField(label='',   widget=forms.Select(attrs={'class':'form-control'}), initial='P', choices=LABEL_CHOICES, required=False)
    icategory       = forms.ModelChoiceField(label='',  queryset=Category.objects.all(), widget=autocomplete.ModelSelect2(url='autocomplete_products:categories:categories_non_sub_all', attrs={'data-placeholder': 'Rechercher la Categorie'}), required=False)
    isubcategory    = forms.ModelChoiceField(label='',  queryset=Category.objects.all(), widget=autocomplete.ModelSelect2(url='autocomplete_products:categories:categories_sub_all', attrs={'data-placeholder': 'Rechercher la Sous-Categorie'}), required=False)
    icolor          = forms.ModelChoiceField(label='',  queryset=Color.objects.all(),    widget=autocomplete.ModelSelect2(url='autocomplete_products:colors:colors_all', attrs={'data-placeholder': 'Rechercher la Couleur', }), required=False)
    isize           = forms.ModelChoiceField(label='',  queryset=Size.objects.all(),     widget=autocomplete.ModelSelect2(url='autocomplete_products:sizes:sizes_all', attrs={'data-placeholder': 'Rechercher la Taille', }), required=False)
    ibool_in_stock  = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title": "In Stock"}), required=False)
    ibool_on_sale   = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title": "On Sale"}),  required=False)
    inew            = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Nouveauté"}),     required=False)
    ibabies         = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Bébés"}),         required=False)
    ichildren       = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Enfants"}),       required=False)
    iteens          = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Adolescents"}),   required=False)
    iadults         = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Adultes"}),       required=False)
    ifemale         = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Femmes"}),        required=False)
    imale           = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Pour Hommes"}),        required=False)
    iunisex         = forms.BooleanField(label='',  widget=forms.CheckboxInput(attrs={"title" : "Unisexe"}),            required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.fields['iqty_stock'].initial       = 1
        self.fields['ibool_in_stock'].initial   = True
        self.fields['ibool_in_stock'].widget.attrs['readonly'] = True
        # self.fields['ibool_in_stock'].widget.attrs['disabled'] = True
from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#CHOICES = [(i,i) for i in range(11)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class wh_CartAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    quantity=forms.IntegerField ( label=("تعداد"),widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':"تعداد" }))

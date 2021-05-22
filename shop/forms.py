from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
class Searchbox (forms.Form):
    searchtxt=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':"جستجو در دوبیچو" }))

from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(label='Enter your text', max_length=100)
    svd = forms.BooleanField(required=False, label='svd')
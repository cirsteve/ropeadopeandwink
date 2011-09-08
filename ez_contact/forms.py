from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField(required=False)
    subject = forms.CharField(max_length=60)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,'cols':10}))

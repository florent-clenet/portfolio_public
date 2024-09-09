# myform/forms.py
from django import forms

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput( 
        attrs={'class': 'form-control width-100%','placeholder': 'Your name','name':"input-name"} ), label="Name")
    company = forms.CharField(max_length=200,widget=forms.TextInput( 
        attrs={'class': 'form-control width-100%', 'placeholder': 'Google, LeadTech','name':"input-company"} ),label="Company and position")
    object = forms.CharField(max_length=200, label="Object",widget=forms.TextInput( 
        attrs={'class': 'form-control width-100%', 'placeholder': '','name':"input-object"} ))
    email = forms.EmailField(label="Email Address",widget=forms.TextInput( 
        attrs={'class': 'form-control width-100%', 'placeholder': 'email@myemail.com','name':"input-email"} ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control width-100%', 'placeholder': 'Your message','name':"message"}), label="Message") 
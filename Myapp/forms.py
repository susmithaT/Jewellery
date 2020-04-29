from django import forms

class Loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)


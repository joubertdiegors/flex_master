from django import forms
from django.contrib.auth.models import User
from customers.models import Customer, Country

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirme a senha')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não coincidem.')
        return cd['password2']

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contact_person_phone', 'contact_person_email', 'country', 'postal_code', 'city', 'address', 'image']

from django import forms
from . import models

class CustomerTypeForm(forms.ModelForm):
    class Meta:
        model = models.CustomerType
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

class CustomerStateForm(forms.ModelForm):
    class Meta:
        model = models.CustomerState
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = [
            'user',
            'name',
            'company_name',
            'customer_type',
            'national_number',
            'tva_number',
            'contact_person_name',
            'contact_person_phone',
            'contact_person_email',
            'general_email',
            'financial_email',
            'country',
            'postal_code',
            'city',
            'address',
            'comments',
            'image',
            'status',
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'national_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tva_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'general_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'financial_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'user': 'Usuário',
            'name': 'Nome',
            'company_name': 'Nome da Empresa',
            'customer_type': 'Tipo de Cliente',
            'national_number': 'Número Nacional',
            'tva_number': 'Número de TVA',
            'contact_person_name': 'Nome da Pessoa de Contato',
            'contact_person_phone': 'Telefone da Pessoa de Contato',
            'contact_person_email': 'Email da Pessoa de Contato',
            'general_email': 'Email Geral',
            'financial_email': 'Email Financeiro',
            'country': 'País',
            'postal_code': 'Código Postal',
            'city': 'Cidade',
            'address': 'Endereço',
            'comments': 'Comentários',
            'image': 'Imagem',
            'status': 'Estado',
        }

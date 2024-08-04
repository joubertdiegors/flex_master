from django import forms
from django.forms.models import inlineformset_factory
from .models import Brand, SalesUnit, PackageUnit, Product, Ingredients, NutritionalItem, NutritionalInfo
from categories import models

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'image']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'name': 'Brand Name',
            'image': 'Brand Image',
        }

class SalesUnitForm(forms.ModelForm):
    class Meta:
        model = SalesUnit
        fields = ['name', 'symbol', 'is_fractional']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unit name'}),
            'symbol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unit symbol'}),
            'is_fractional': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'name': 'Unit Name',
            'symbol': 'Unit Symbol',
            'is_fractional': 'Is Fractional?',
        }

class PackageUnitForm(forms.ModelForm):
    class Meta:
        model = PackageUnit
        fields = ['name', 'symbol']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unit name'}),
            'symbol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unit symbol'}),
        }
        
        labels = {
            'name': 'Unit Name',
            'symbol': 'Unit Symbol',
        }

class ProductForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'id_category', 'style': 'height: 300px;'}),
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'barcode',
            'name',
            'volume',
            'package_unit',
            'brand',
            'country',
            'category',
            'sales_unit',
            'net_weight',
            'gross_weight',
            'stock_control',
            'minimum_stock',
            'maximum_stock',
            'selling_price',
            'image',
            'description',
            'is_active'
        ]

        widgets = {
            'barcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter barcode'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter net volume'}),
            'package_unit': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'sales_unit': forms.Select(attrs={'class': 'form-control'}),
            'net_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter net weight'}),
            'gross_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter gross weight'}),
            'stock_control': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'stockControlSwitch'}),
            'minimum_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minimum stock'}),
            'maximum_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter maximum stock'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter selling price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'isActiveSwitch'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = self.get_category_choices()

    def get_category_choices(self):
        categories = models.Category.objects.all()
        category_choices = []

        def add_children(categories, level=0):
            for category in categories:
                category_choices.append((category.id, f"{'--' * level} {category.name}"))
                add_children(category.subcategories.all(), level + 1)

        add_children(categories.filter(parent=None))
        return category_choices

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['product', 'ingredients', 'allergens', 'conservation_instructions']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'allergens': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'conservation_instructions': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class NutritionalItemForm(forms.ModelForm):
    class Meta:
        model = NutritionalItem
        fields = ['name', 'package_unit']

class NutritionalInfoForm(forms.ModelForm):
    class Meta:
        model = NutritionalInfo
        fields = ['nutritional_item', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'step': '0.01'}),
        }

NutritionalInfoFormSet = inlineformset_factory(
    Product,
    NutritionalInfo,
    form=NutritionalInfoForm,
    extra=1,
    can_delete=True
)

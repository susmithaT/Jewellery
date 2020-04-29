from django import forms
from .models import Order, Material, Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'



class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

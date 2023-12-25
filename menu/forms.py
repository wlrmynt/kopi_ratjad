from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Menu

class formLogin(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {'class':'form-control'}))

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('nama_product', 'harga', 'status')
        labels = {
            'nama_product': ('Nama Product'),
            'harga': ('Harga'),
            'status': ('Status')
            }
        error_messages ={
        'nama_product':{
            'required':_("Nama Product Harus diisi")
        },
        'harga':{
            'required':_("Harga Harus diisi")
        },
        }
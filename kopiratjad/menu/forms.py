from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Menu
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class formLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {'class':'form-control'}))


class RegisterForm(UserCreationForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs= {'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {'class':'form-control'}))


    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields+('first_name','last_name', 'username','email', 'password1', 'password2')
    def save(self, commit=True) :
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']





        if commit :
            user.save()
        return user


class MenuForm(ModelForm):

    class Meta:
        model = Menu
        fields = ('nama_product', 'harga', 'air','jenis_gilingan_biji_kopi','takaran_gula', 'takaran_susu', 'takaran_soda','takaran_marjan','keterangan','status')
        labels = {
            'nama_product': ('Nama Product'),
            'harga': ('Harga'),
            'air': ('air'),
            'jenis_gilingan_biji_kopi': ('Jenis Gilingan Biji'),
            'takaran_gula': ('Takaran Gula'),
            'takaran_susu': ('Takaran susu'),
            'takaran_soda': ('Takaran Soda'),
            'takaran_marjan': ('Takaran Marjan'),
            'keterangan': ('Keterangan'),
            'status': ('Status')
            }
        error_messages ={
        'nama_product':{
            'required':_("Nama Product Harus diisi")
        },
        'harga':{
            'required':_("Harga Harus diisi")
        },
        'air':
         { 
             'required':('Takaran air harus di isi')},

        'jenis_gilingan_biji_kopi':
        {   'required': ('Jenis Gilingan BijiHarus Diisi atau kasih tanda (-)')},
        
        'takaran_gula': 
        { 'required': ('Takaran Gula Harus Diisi atau kasih tanda (-)')},

        'takaran_susu': 
        { 'required':('Takaran susu Harus Diisi atau kasih tanda (-)')},
        'takaran_soda':
         {'required': ('Takaran Soda Harus Diisi atau kasih tanda (-)')},
        'takaran_marjan':
         {'required': ('Takaran Marjan Harus Diisi atau kasih tanda (-)')},
        'keterangan':
         {'required': ('Harus Mengisi Keterangan')},
        
        }


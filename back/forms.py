from django.forms import ModelForm
from .models import MyUser
from django.utils.translation import gettext_lazy as _
from django import forms

class MyUserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        labels = {
            'username': _('Username'),
            'password': _('Password')
                    }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }
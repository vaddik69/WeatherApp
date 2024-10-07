from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import City
from django.forms import ModelForm, TextInput, CharField, PasswordInput
import re
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import messages


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}


class UserRegistrationForm(ModelForm):
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Repeat password', widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': _('Login')})
        self.fields['first_name'].widget.attrs.update({'placeholder': _('First name')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Email')})
        self.fields['password'].widget.attrs.update({'placeholder': _('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': _('Confirm password')})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2')

    def clean_password2(self):
        pattern_password = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
        cd = self.cleaned_data
        if not bool(pattern_password.match(cd['password'])):
            raise ValidationError('The password must contain uppercase and lowercase Latin letters, numbers and be no '
                                  'shorter than 8 characters.')
        elif cd['password'] != cd['password2']:
            raise ValidationError('Passwords don`t match.')
        return cd['password2']


from dataclasses import fields
from django import forms 
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email', 'phone_number', ]


class AccountAuthentificationForm(forms.ModelForm):
    # mail = forms.EmailField(max_length=60, help_text='valid email kiriting!')
    password = forms.CharField(label='password', widget = forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid inputs")


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [ 'f_name', 'l_name', 'sex', 'date_birthday']
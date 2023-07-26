from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django import forms
from django import forms
from app2.models import District, Branch, Material,Account



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [ "username", "password1", "password2"]
        widgets = {
            # "password": forms.PasswordInput(attrs={"class": "form-control"}),  # tohash password
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


# forms.py



class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type', 'materials_provide']









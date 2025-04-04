from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from users.models import CustomUser


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise ValidationError(gettext("Passwords are not the same."), code="invalid")
        return cleaned_data

    class Meta:
        model = CustomUser
        fields = ["email", "phone_number", "password"]
        widgets = {
            "email": forms.widgets.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "password": forms.widgets.PasswordInput(attrs={"class": "form-control"}),
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}))

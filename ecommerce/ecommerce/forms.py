from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'id': 'form_full_name'
            })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            })
    )
# Checks if email has gmail or not

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be Gmail')
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
        }))


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
        }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
        }))
# Checks if username exists in query set

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
# Checks if email exists in query set

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords Must Match')
        return data

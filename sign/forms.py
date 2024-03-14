from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control', 'autocomplete': 'off'})

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError('Email already in use.')
            return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['slug', 'image', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'})
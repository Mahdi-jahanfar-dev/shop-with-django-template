from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'enter password1'}))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'enter password2'}))

    class Meta:
        model = User

        fields = ['email', 'phone_number']

    def clean_password2(self):

        cleaned_data = self.cleaned_data

        if cleaned_data['password'] and cleaned_data['password2'] and cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords do not match')


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

class UserUpdateForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text='you can change your password with this <a href=\"../password/ \">link</a>')

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name', 'password']


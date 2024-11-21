from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'placeholder': 'enter password1'}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'placeholder': 'enter password2'}))

    class Meta:
        model = User

        fields = ['email', 'phone_number']

    def clean_password2(self):

        cleaned_data = self.cleaned_data

        if self.cleaned_data.get('password1') and self.cleaned_data.get('password2') and self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            raise ValidationError('Passwords do not match')

        return cleaned_data.get('password2')


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
            
        return user

class UserUpdateForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text='you can change your password with this <a href=\"../password/\">link</a>')

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name', 'password']



class RegisterForm(forms.Form):

    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')

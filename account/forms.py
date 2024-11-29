from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User,OtpCode


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password1', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ['email', 'phone_number']

    def clean_password2(self):

        cleaned_data = self.cleaned_data

        if self.cleaned_data.get('password1') and self.cleaned_data.get('password2') and self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data.get('password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) > 11:
            raise forms.ValidationError('this phone number is too long')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('this phone number is already exists')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is already exists')

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


class RegistrationCodeForm(forms.Form):
    code = forms.IntegerField()

    def clean_code(self):
        otp = OtpCode.objects.filter(code=self.cleaned_data.get('code')).exists()
        if otp is None:
            raise forms.ValidationError('this code is wrong, please try again')


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11, label='phone number')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')


    def clean(self):
        user = authenticate(phone_number=self.cleaned_data.get('phone_number'), password=self.cleaned_data.get('password'))

        if user is None:
            raise forms.ValidationError('this phone number or password is incorrect')

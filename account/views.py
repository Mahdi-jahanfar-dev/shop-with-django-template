from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from . import forms
import Utils
from .models import OtpCode, User
import random



class UserRegisterView(View):

    form_class = forms.UserCreationForm

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('home:home')

        form = self.form_class()
        return render(request, 'account/register.html', {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = random.randint(1000, 9999)
            phone_number = form.cleaned_data['phone_number']
            Utils.sent_otp_code(phone_number, code)
            OtpCode.objects.create(phone_number=phone_number, code=code)
            request.session['user_registration_info'] = {
                'phone_number': phone_number,
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],
                'code': code
            }
            return redirect('account:register_code')
        return render(request, 'account/register.html', {'form': form})



class UserRegisterCodeView(View):

    from_class = forms.RegistrationCodeForm

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('home:home')

        form = self.from_class()
        return render(request, 'account/registration_form.html', {'form': form})

    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            phone_number = request.session['user_registration_info']['phone_number']
            if code == request.session['user_registration_info']['code']:
                User.objects.create(phone_number=phone_number, email=request.session['user_registration_info']['email'], password=request.session['user_registration_info']['password'])
                otp_c = OtpCode.objects.get(phone_number=phone_number)
                otp_c.delete()
                return redirect('home:home')
            else:
                return render(request, 'account/registration_form.html', {'form': form})
        return render(request, 'account/registration_form.html', {'form': form})


class UserLoginView(View):
    form_class = forms.LoginForm

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('home:home')

        form = self.form_class()
        return render(request, 'account/login.html', {'form': form})


    def post(self, request):
        
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.get(phone_number=form.cleaned_data.get('phone_number'),)

            login(request, user)

            return redirect('home:home')

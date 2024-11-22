from django.shortcuts import render, redirect
from django.views import View
from . import forms
import Utils
from .models import OtpCode
import random
class UserRegisterView(View):

    form_class = forms.RegisterForm

    def get(self, request):
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
                'password': form.cleaned_data['password']
            }
            return redirect('account:register_code')
        return redirect('account:register')



class UserRegisterCodeView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

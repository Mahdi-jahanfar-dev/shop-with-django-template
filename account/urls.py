from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('register_code', views.UserRegisterCodeView.as_view(), name='register_code')
]
from django.urls import path
from .views import HomePageView, ProductDetailView

app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail')

]
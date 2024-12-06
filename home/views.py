from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView
from .models import Product

class HomePageView(View):

    recent_products = Product.objects.all()[:4]



    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name, {'recent_products': self.recent_products, })


class ProductDetailView(DetailView):
    model = Product
    Template_name = 'home/product_detail.html'
    context_object_name = 'product'


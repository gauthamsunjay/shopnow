from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProductListView(LoginRequiredMixin, ListView):
  model = Product
  template_name = "products/products.html"
  products = []

  def get_queryset(self):
    return [{
      'category': 'Cycles',
      'products': [{
        'name': 'Cycle-1',
        'price': '800',
        'num_left': 4,
        'image': 'product_1.jpg'
      }]
    }, {
      'category': 'Ford Cycles',
      'products': [{
        'name': 'Cycle-2',
        'price': '2000',
        'num_left': 2,
        'image': 'product_2.jpeg'
      }]
    }]

class ProductDetailView(DetailView):
  model = Product
  template_name = "products/detail_view.html"
  queryset = model.objects.all()

  def get_queryset(self, *args, **kwargs):
    pk = kwargs.get("pk", 1)
    return Product.objects.filter(id=pk)

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.


class ProductListView(ListView):
  model = Product
  template_name = "products/list_view.html"


class ProductDetailView(DetailView):
  model = Product
  template_name = "products/detail_view.html"
  queryset = model.objects.all()

  def get_queryset(self, *args, **kwargs):
    pk = kwargs.get("pk", 1)
    return Product.objects.filter(id=pk)

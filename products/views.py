from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def get_products(query):
  products = {}
  objects = Product.objects.all()
  if query:
    objects = objects.filter(name__icontains=query)

  for obj in objects:
    try:
      products[obj.category].append(
        {
          "name": obj.name,
          "price": obj.price,
          "num_left": obj.num_left,
          "image": obj.image
        }
      )

    except KeyError:
      products[obj.category] = [{
        "name": obj.name,
        "price": obj.price,
        "num_left": obj.num_left,
        "image": obj.image
      }]

  return [{"category": k, "products": v} for k, v in products.iteritems()]


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
    }]


class ProductsSearchView(ListView):
  model = Product
  template_name = "products/search.html"
  queryset = Product.objects.all()

  def get_queryset(self):
    query = self.request.GET.get("q", None)
    return get_products(query)


class ProductDetailView(DetailView):
  model = Product
  template_name = "products/detail_view.html"
  queryset = model.objects.all()

  def get_queryset(self, *args, **kwargs):
    pk = kwargs.get("pk", 1)
    return Product.objects.filter(id=pk)

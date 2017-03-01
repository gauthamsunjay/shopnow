from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.views import View
from cart.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def get_products(query=None):
  products = {}
  objects = Product.objects.all()
  if query:
    objects = objects.filter(name__icontains=query)

  for obj in objects:
    try:
      products[obj.category].append(
        {
          "id": obj.pk,
          "name": obj.name,
          "price": obj.price,
          "num_left": obj.num_left,
          "image": obj.image
        }
      )

    except KeyError:
      products[obj.category] = [{
        "id": obj.pk,
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
    return get_products()


class ProductsSearchView(ListView):
  model = Product
  template_name = "products/products.html"
  queryset = Product.objects.all()

  def get_queryset(self):
    query = self.request.GET.get("q", None)
    return get_products(query=query)


class ProductDetailView(DetailView):
  model = Product
  template_name = "products/detail_view.html"
  queryset = model.objects.all()

  def get_queryset(self, *args, **kwargs):
    pk = kwargs.get("pk", 1)
    return Product.objects.filter(id=pk)


class ProductCartView(LoginRequiredMixin, View):
  def post(self, request, *args, **kwargs):
    pk = kwargs.get("pk")
    product = Product.objects.get(pk=pk)
    try:
      cart = Cart.objects.get(user=request.user)
      cart.products.add(product)
      cart.save()

    except Cart.DoesNotExist:
      cart = Cart(user=request.user)
      cart.save()
      cart.products.add(product)
      cart.save()

    return JsonResponse({"success": True}, safe=False)

  def delete(self, request, *args, **kwargs):
    pk = kwargs.get("pk")
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart.products.remove(product)
    cart.save()

    return JsonResponse({"success": True}, safe=False)

from django.http.response import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart as model

# Create your views here.


class CartView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    try:
      cart = model.objects.get(user=request.user)
      products = cart.products.all()
      data = []
      for product in products:
        data.append({
          'name': product.name,
          'price': product.price,
          'image': product.image
        })

      reply = {"data": data, "success": True}

    except:
      reply = {"data": [], "success": False}

    return JsonResponse(reply, safe=False)

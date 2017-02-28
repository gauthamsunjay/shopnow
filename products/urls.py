from django.conf.urls import url, include
from .views import ProductCartView, ProductDetailView
from django.views.generic.base import RedirectView

urlpatterns = [
  url(r"^$", RedirectView.as_view(url="/")),
  url(r"^(?P<pk>\d+)/$", ProductDetailView.as_view(), name="detail"),
  url(r"^add_to_cart/(?P<pk>\d+)/$", ProductCartView.as_view())
]


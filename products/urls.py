from django.conf.urls import url, include
from .views import ProductDetailView, ProductListView
from django.views.generic.base import RedirectView

urlpatterns = [
  url(r"^$", RedirectView.as_view(url="/")),
  url(r"^(?P<pk>\d+)/$", ProductDetailView.as_view(), name="detail"),
]


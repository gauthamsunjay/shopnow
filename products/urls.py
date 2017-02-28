from django.conf.urls import url, include
from .views import ProductDetailView, ProductListView

urlpatterns = [
  url(r"^$", ProductListView.as_view(), name="list"),
  url(r"^(?P<pk>\d+)/$", ProductDetailView.as_view(), name="detail"),
]


"""shopnow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from products.views import ProductListView, ProductsSearchView
from .views import home

urlpatterns = [
    # url(r'/$', home, name="home"),
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include("products.urls")),
    url(r'^search$', ProductsSearchView.as_view(), name="search"),
    url(r'^accounts/', include("accounts.urls")),
    url('^', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

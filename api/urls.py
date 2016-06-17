from django.conf.urls import url, include
from django.contrib import admin
from api.views import ProductList, ProductDetail, CategoryList

urlpatterns = [
    url(r'^products/$', ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),
    url(r'^categories/$', CategoryList.as_view()),
]

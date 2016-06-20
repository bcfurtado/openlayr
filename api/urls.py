from django.conf.urls import url, include
from django.contrib import admin
from api.views import ProductList, ProductDetail, CategoryList, CategoryDetail, OrderList

urlpatterns = [
    url(r'^products/$', ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),
    url(r'^categories/$', CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
    url(r'^orders/$', OrderList.as_view()),
]

from django.conf.urls import url, include
from django.contrib import admin
from api.views import ProductList

urlpatterns = [
    url(r'^products/$', ProductList.as_view()),
]

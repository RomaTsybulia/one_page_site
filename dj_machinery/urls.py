from django.urls import path, include

from dj_machinery import views

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("transport/", views.TransportList.as_view()),
]

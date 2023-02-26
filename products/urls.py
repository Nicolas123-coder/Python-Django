from django.urls import path, include
from . import views

urlpatterns = [
    path('see_product/', views.see_product, name='see_product'),
    path('create_product/', views.create_product, name='create_product')
]

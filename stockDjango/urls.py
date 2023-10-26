from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-details/<int:id>/', views.product_details, name='product_details'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product')
]
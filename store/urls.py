from django.urls import path
from . import views

urlpatterns = [
    path('', views.showStore, name='show-store'),
    path('<slug:category_slug>/', views.showStore, name='products-by-category'),
    path('<slug:category_slug>/<slug:product_slug>',
         views.productDetail, name='product-detail')

]

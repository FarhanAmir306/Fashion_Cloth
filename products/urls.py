from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView,ProductView,BestSellerView,AcceptProductView

router = DefaultRouter()
router.register('categories', CategoryView, basename='category')
router.register('products', ProductView, basename='products')
router.register('bestseller', BestSellerView, basename='bestseller')
router.register('accept_product', AcceptProductView, basename='accept_product')

urlpatterns = [
    path('', include(router.urls)),
]
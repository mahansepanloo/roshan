from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('accounts.urls', namespace="auth-token")),
    path('api/products/', include('products.urls', namespace="products-api")),
    path('api/cart/', include('carts.urls', namespace="cart-api")),
    path("api/categories/", include('categories.urls', namespace="category-api")),


]

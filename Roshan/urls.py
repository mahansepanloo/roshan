from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth', include('accounts.urls'), namespace="auth-token"),
    path('api/', include('products.urls'), namespace="products-api"),
    path('api/cart', include('carts.urls'), namespace="cart-api"),

]

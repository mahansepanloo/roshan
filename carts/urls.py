from django.urls import path
from . import views

app_name = 'cart-api'
urlpatterns = [
    path('',views.CartViews.as_view(),name='cart'),
    path("add/<int:product_id>/",views.AddViews.as_view(),name='add'),
    path("remove/<int:product_id>/", views.RemoveViews.as_view(), name='remove'),
    path("clear/", views.ClearViews.as_view(), name='clear'),

]

from django.urls import path
from . import views


app_name = '"products-api"'
urlpatterns = [
    path("",views.AddProductsView.as_view(),name="show_and_add"),
    path('<int:id>',views.EditedProductsView.as_view(),name="edit_product"),
]
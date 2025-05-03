from django.urls import path
from . import views

app_name = "category-api"
urlpatterns = [
    path("", views.AddShowCategorysViews.as_view(), name="category-list"),
    path("<int:pk>", views.EditDeleteCategoryViews.as_view(), name="category-list"),
    path("<int:id>/products/", views.ShowAddPCategoryViews.as_view(), name="product"),
]

from django.urls import path
from . import views


app_name = '"products-api"'
urlpatterns = [
    path("", views.AddProductsView.as_view(), name="show_and_add"),
    path('<int:id>', views.EditedProductsView.as_view(), name="edit_product"),
    path("comment/<int:id_product>", views.CommentView.as_view(), name="comment"),
    path("reply/<int:id_comment>/<int:id_product>", views.ReplyCommentView.as_view(), name='reply'),
]
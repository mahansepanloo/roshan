from celery.bin.control import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from products.models import ProductsModel
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .carts import Cart

class CartViews(APIView):
    """
    show cart
    """
    def get(self, request):
        carts = Cart(request)
        data = carts.cart
        return Response(data,status=status.HTTP_200_OK)



class AddViews(APIView):
    """
    add cart
    """
    serializers_class = AddCartSerializer
    def post(self, request, product_id):
        product = get_object_or_404(ProductsModel, id=product_id)
        carts = Cart(request)
        serializer = AddCartSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['num']
            carts.add(product, quantity)
            return Response("add cart", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RemoveViews(APIView):
    """
    remove product from cart
    """
    def delete(self, request, product_id):
        product = get_object_or_404(ProductsModel, id=product_id)
        carts = Cart(request)
        carts.remove_product(product)
        return Response("remove products cart", status=status.HTTP_204_NO_CONTENT)


class ClearViews(APIView):
    """
    clear cart
    """
    def delete(self, request):
        carts = Cart(request)
        carts.clear()
        return Response('delete cart', status=status.HTTP_204_NO_CONTENT)


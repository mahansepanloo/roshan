from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from .serializers import *
from products.models import ProductsModel
from rest_framework import status
from django.shortcuts import get_object_or_404





class AddProductsView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(AddProductsView, self).get_permissions()

class EditedProductsView(APIView):
    def setup(self, request, *args, **kwargs):
        self.product = get_object_or_404(ProductsModel, id=kwargs['id'])
        return super().setup( request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer(self.product)
        self.product.views += 1
        self.product.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer2(instance = self.product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)
        self.product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    """
   just admin can create products and see all products
    """
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(AddProductsView, self).get_permissions()

class EditedProductsView(APIView):
    serializer_class = ProductSerializer
    def setup(self, request, *args, **kwargs):
        self.product = get_object_or_404(ProductsModel, id=kwargs['id'])
        return super().setup( request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        see products
        """
        ip = get_ip(request)
        user = ViewssModel.objects.filter(userip=ip)
        if not user.exists():
            ViewssModel.objects.create(userip=ip, product = self.product)
            self.product.views += 1
            self.product.save()
        serializer = ProductSerializer(self.product)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    def put(self, request, *args, **kwargs):
        """
        admin can edit products
        """
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer2(instance = self.product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        admin can delete products
        """
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)
        self.product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

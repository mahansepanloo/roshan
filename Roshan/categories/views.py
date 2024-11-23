from celery.bin.control import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import action, permission_classes
from .serializers import *
from rest_framework import status




class AddShowCategorysViews(generics.ListCreateAPIView):
    """
    post : admin create category
    get : all user see categories
    """
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoryCSerializer
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(AddShowCategorysViews, self).get_permissions()


class EditDeleteCategoryViews(generics.RetrieveUpdateDestroyAPIView):
    """
    admin edit and delete category
    """

    queryset = CategoriesModel.objects.all()
    serializer_class = CategoryESerializer
    permission_classes = [IsAdminUser]

class ShowAddPCategoryViews(APIView):

    def setup(self, request, *args, **kwargs):
        self.category = get_object_or_404(CategoriesModel, id = kwargs['id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        see all categories
        """
        serializer_class = ShowProductCategorySerializer
        product = ShowProductCategorySerializer(instance=self.category)
        return Response(data = product.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        admin add product to category
        """
        serializer_class = AddProductCategorySerializer
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to perform this action.'},
                status=status.HTTP_403_FORBIDDEN)
        serializer = AddProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product')
            try:
                product = ProductsModel.objects.get(id=product_id)
            except ProductsModel.DoesNotExist:
                return Response({'detail': 'Product not found.'},status=status.HTTP_404_NOT_FOUND)
            self.category.product.add(product)
            return Response({'detail': 'Product added to category successfully.'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)








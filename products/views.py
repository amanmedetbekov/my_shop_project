# from warnings import _catch_warnings_with_records
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     RetrieveAPIView, UpdateAPIView,
                                     DestroyAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from products.filters import ProductPriceFilters
from .models import Product, Comment
from .serializers import ProductListSerializer, ProductSerializer, CommentSerializer
from .permissions import IsAuthor


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdatesView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filterset_fields = ['category']
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    filterset_class = ProductPriceFilters
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy','update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()


# post -> 'create'
# get -> 'list', 'retrieve'
# put -> 'update'
# patch -> 'partial_update'
# delete -> 'destroy'


# TODO: ???????????????? ???? ?????????? ?????????????? 
# TODO: ?????????????????????? ???????????? ?? ???????????? 
# TODO: ???????????????? ??????????
# TODO: FastAPI
# TODO: Doker
# TODO: Async
# TODO: pytest

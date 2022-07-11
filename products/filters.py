from cgitb import lookup
from dataclasses import field
from django_filters import rest_framework as filters
from .models import Product


class ProductPriceFilters(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price',
                                      lookup_expr='gte')

    price_to = filters.NumberFilter(field_name='price',
                                    lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category']

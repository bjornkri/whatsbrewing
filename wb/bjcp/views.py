from rest_framework import viewsets
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer, Stat


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows subcategories to be viewed.
    """
    queryset = SubCategory.objects.all().order_by('id')
    serializer_class = SubCategorySerializer
    lookup_field = 'code'

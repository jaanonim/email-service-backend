from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Group
from .serializers import GroupSerializer


class FilterGroupView(ListAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ("name",)
    ordering_fields = ("name",)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

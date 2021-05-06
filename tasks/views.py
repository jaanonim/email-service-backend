from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer


class FilterTaskView(ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ("name", "status", "group__name", "term")
    ordering_fields = ("name", "status", "term")

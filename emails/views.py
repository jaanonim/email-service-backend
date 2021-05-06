from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Email
from .serializers import EmailSerializer


class FilterEmailView(ListAPIView):

    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ("name", "email", "group__name")
    ordering_fields = (
        "name",
        "email",
        "group__name",
    )

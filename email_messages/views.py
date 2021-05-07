from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Message
from .serializers import MessageSerializer


class FilterMessageView(ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ("name", "title")
    ordering_fields = (
        "name",
        "title",
    )

class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


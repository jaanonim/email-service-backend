from django.urls import path

from .views import *

urlpatterns = [
    path("", MessageViewSet.as_view({"get": "list", "post": "create"})),
    path("filter/", FilterMessageView.as_view()),
    path(
        "<uuid:pk>/",
        MessageViewSet.as_view({"delete": "destroy", "patch": "partial_update"}),
    ),
]

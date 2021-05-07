from django.urls import path

from .views import *

urlpatterns = [
    path("", GroupViewSet.as_view({"get": "list", "post": "create"})),
    path("filter/", FilterGroupView.as_view()),
    path(
        "<uuid:pk>/",
        GroupViewSet.as_view({"delete": "destroy", "patch": "partial_update"}),
    ),
]

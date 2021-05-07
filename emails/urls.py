from django.urls import path

from .views import *

urlpatterns = [
    path("", EmailViewSet.as_view({"get": "list", "post": "create"})),
    path("filter/", FilterEmailView.as_view()),
    path(
        "<uuid:pk>/",
        EmailViewSet.as_view({"delete": "destroy", "patch": "partial_update"}),
    ),
]

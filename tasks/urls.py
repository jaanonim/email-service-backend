from django.urls import path

from .views import *

urlpatterns = [
    path("", TaskViewSet.as_view({"get": "list", "post": "create"})),
    path("filter/", FilterTaskView.as_view()),
    path(
        "<uuid:pk>/",
        TaskViewSet.as_view({"delete": "destroy", "patch": "partial_update"}),
    ),
]

from django.urls import path

from .views import FilterGroupView

urlpatterns = [path("", FilterGroupView.as_view())]

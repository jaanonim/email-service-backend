from django.urls import path

from .views import FilterMessageView

urlpatterns = [path("", FilterMessageView.as_view())]

from django.urls import path

from .views import FilterTaskView

urlpatterns = [path("", FilterTaskView.as_view())]

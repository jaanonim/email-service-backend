from django.urls import path

from .views import FilterEmailView

urlpatterns = [path("", FilterEmailView.as_view())]

"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import connection
from django.urls import include, path
from email_messages import urls as messageUrls
from emails import urls as emailUrls
from groups import urls as groupUrls
from tasks import urls as taskUrls

urlpatterns = [
    path("messages/", include(messageUrls)),
    path("emails/", include(emailUrls)),
    path("groups/", include(groupUrls)),
    path("tasks/", include(taskUrls)),
]


def table_exists(table_name):
    try:
        return table_name in connection.introspection.table_names()
    except Exception as e:
        return False


if table_exists("tasks_task"):
    from .schedule import startTreading

    startTreading()

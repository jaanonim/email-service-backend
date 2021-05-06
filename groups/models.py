import uuid

from django.db import models

from .validators import color


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6, validators=[color], default="000000")
    description = models.TextField(default="", blank=True, null=True)

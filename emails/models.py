import uuid

from django.db import models


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.ManyToManyField("groups.group", blank=True)

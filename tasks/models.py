import uuid

from django.db import models

STAUS_OPTIONS = ((1, "waiting"), (2, "processing"), (3, "done"), (4, "fail"))


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)
    status = models.IntegerField(choices=STAUS_OPTIONS, editable=False, default=1)
    term = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(
        "groups.group", on_delete=models.CASCADE, blank=True, null=True
    )
    message = models.ForeignKey("email_messages.message", on_delete=models.CASCADE)

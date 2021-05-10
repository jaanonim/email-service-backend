import uuid

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from emails.models import Email

from .email import sendEmailThread

STAUS_OPTIONS = ((1, "waiting"), (2, "processing"), (3, "done"), (4, "fail"))


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)
    status = models.IntegerField(choices=STAUS_OPTIONS, editable=False, default=1)
    term = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(
        "groups.group", on_delete=models.CASCADE, blank=True, null=True
    )
    message = models.ForeignKey("email_messages.message", on_delete=models.CASCADE)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        self.on_update()

    def delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)
        self.on_update()

    def execute(self):
        print("Excuted", self.name)
        emails = []

        if self.group:
            emails_obj = self.group.email_set.all()
        else:
            emails_obj = Email.objects.all()
        for obj in emails_obj:
            emails.append(obj.email)

        sendEmailThread(
            title=self.message.title,
            message=self.message.content,
            email_addres=emails,
            task=self,
        )

    def on_update(self):
        from app.schedule import s

        s.updateList()

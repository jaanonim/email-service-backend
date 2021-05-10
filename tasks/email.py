import threading

from django.core.mail import EmailMessage


def sendEmailThread(message, title, email_addres, task):
    thread = myThread(
        1,
        "Sending Email",
        task=task,
        message=message,
        title=title,
        email_addres=email_addres,
    )
    thread.start()


class myThread(threading.Thread):
    def __init__(self, threadID, name, task, message, title, email_addres):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.message = message
        self.title = title
        self.email_addres = email_addres
        self.task = task

    def run(self):
        self.sendEmail()

    def sendEmail(self):
        email = EmailMessage(self.title, self.message, to=self.email_addres)
        email.content_subtype = "html"
        try:
            email.send()
        except Exception as e:
            print("Error", self.task.name, ":", e)
            self.task.status = 4
            self.task.save()
        else:
            print("Sucess", self.task.name)
            self.task.status = 3
            self.task.save()

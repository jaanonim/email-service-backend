import threading
import time

from django.conf import settings
from django.utils import timezone
from tasks.models import Task

import schedule


class ScheduleTasks:
    def __init__(self):
        self.tasks = []
        self.updateList()

    def updateList(self):

        print("updating ...")

        self.tasks = Task.objects.filter(status=1)
        self.checkForTask()

    def checkForTask(self):
        print("cheking ...")

        for task in self.tasks:
            if task.term < timezone.now():
                thread = threading.Thread(
                    target=task.execute, name="Executing task: " + task.name
                )
                thread.start()
                task.status = 2
                task.save()


s = ScheduleTasks()


def treadFunction():
    schedule.every().minutes.do(s.checkForTask)

    while True:
        schedule.run_pending()
        time.sleep(10)


def startTreading():
    thread = threading.Thread(target=treadFunction, name="schedule")
    thread.start()

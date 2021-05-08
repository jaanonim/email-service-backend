import threading
import time

from django.utils import timezone
from tasks.models import Task

import schedule

tasks = []


def updateList():
    global tasks

    print("updating ...")

    tasks = Task.objects.filter(status=1)
    print(tasks)


def checkForTask():
    print("cheking ...")

    for task in tasks:
        print(task.term, timezone.now(), task.term < timezone.now())
        if task.term < timezone.now():
            thread = threading.Thread(
                target=task.execute, name="Executing task: " + task.name
            )
            thread.start()
            task.status = 2
            task.save()


def treadFunction():
    updateList()
    checkForTask()

    schedule.every().minutes.do(checkForTask)

    while True:
        schedule.run_pending()
        time.sleep(10)


def startTreading():
    thread = threading.Thread(target=treadFunction, name="schedule")
    thread.start()

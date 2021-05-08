import threading
import time

import schedule


def updateList():
    print("updating ...")


def checkForTask():
    print("cheking ...")


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

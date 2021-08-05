import time
from win10toast import ToastNotifier
import datetime

def gettimeinput():
    hour=int(input('hours of interval:  '))
    Minutes=int(input('Minutes of interval:  '))
    Seconds=int(input('seconds of interval:  '))
    time_interval=Seconds+(Minutes*60)+(hour*3600)
    return time_interval

def log():
    now=datetime.datetime.now()
    start_time=now.strftime("%H:%M:%S")
    with open("log.txt",'a'):
        f.write("You drank water {now} \n")
    return 0

def notify():
    notification=ToastNotifier()
    notification.show_toast("Time to drink water")
    log()
    return 0

def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()

if __name__=='__main__':
    time_interval=gettimeinput()
    starttime(time_interval)
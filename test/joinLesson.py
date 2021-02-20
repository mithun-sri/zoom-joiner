from zoom_joiner.test.addTimetable import GetCurrentSchedule
import webbrowser
from datetime import datetime
import time
from zoom_joiner.test.readLesson import ReadLessons
schedule = GetCurrentSchedule()

def OpenLink(lessonName):
    Lessons = ReadLessons()
    for x in range(len(Lessons)):
        for name,link in Lessons[x].items():
            if name == lessonName:
                lessonLink = link
    webbrowser.open(lessonLink)
    print("Opened link.")

def Sleep(lessonTime,lessonName):
    now = datetime.now()
    currentDate = datetime.now().strftime("%Y-%m-%d ")
    reqTime = datetime.strptime(str(currentDate+lessonTime),"%Y-%m-%d %H:%M:%S")
    timeRemaining = (reqTime-now).seconds
    time.sleep(timeRemaining)
    OpenLink(lessonName)
    
def MaintainSchedule():
    for x in range(len(schedule)):
        lessonTime = schedule[x].split(',')[0]
        lessonName = schedule[x].split(',')[1]
        now = datetime.now()
        currentDate = datetime.now().strftime("%Y-%m-%d ")
        reqTime = datetime.strptime(str(currentDate+lessonTime),"%Y-%m-%d %H:%M:%S")
        
        if now > reqTime:
            print(schedule[x].split(',')[1] + " is over.")
            
        elif now < reqTime:
            Sleep(lessonTime,lessonName)
        

MaintainSchedule()

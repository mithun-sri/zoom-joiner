from zoom_joiner.test.add_timetable import GetCurrentSchedule
import webbrowser
from datetime import datetime
import time
from zoom_joiner.test.read_lesson import ReadLessons
schedule = GetCurrentSchedule()

def open_link(lessonName):
    Lessons = ReadLessons()
    for x in range(len(Lessons)):
        for name,link in Lessons[x].items():
            if name == lessonName:
                lessonLink = link
    webbrowser.open(lessonLink)
    print("Opened link.")

def sleep(lessonTime,lessonName):
    now = datetime.now()
    currentDate = datetime.now().strftime("%Y-%m-%d ")
    reqTime = datetime.strptime(str(currentDate+lessonTime),"%Y-%m-%d %H:%M:%S")
    timeRemaining = (reqTime-now).seconds
    time.sleep(timeRemaining)
    open_link(lessonName)
    
def maintain_schedule():
    for x in range(len(schedule)):
        lessonTime = schedule[x].split(',')[0]
        lessonName = schedule[x].split(',')[1]
        now = datetime.now()
        currentDate = datetime.now().strftime("%Y-%m-%d ")
        reqTime = datetime.strptime(str(currentDate+lessonTime),"%Y-%m-%d %H:%M:%S")
        
        if now > reqTime:
            print(schedule[x].split(',')[1] + " is over.")
            
        elif now < reqTime:
            sleep(lessonTime,lessonName)
        
if __name__ == "__main__":
    maintain_schedule()

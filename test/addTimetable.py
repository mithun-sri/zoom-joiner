import datetime

def GetCurrentSchedule():
    today = datetime.datetime.today().weekday()

    f_timetable = open("ZoomJoiner/timetable.txt","r")
    
    dayCount = -1
    lines = []
    for line in f_timetable:
        lines.append(line)
    

    x = 0
    while dayCount!=today:
        if lines[x][0:-1] == "NewDay":
            dayCount+=1
        x+=1
    f_timetable.close()
    
    isReady = False
    reqTimetable = []

    while isReady == False:        
        if (lines[x][0:-1] == "NewDay") or  (lines[x] =="end"):
            isReady = True
        else:
            reqTimetable.append(lines[x][0:-1])
        x+=1
    
    return reqTimetable
    
                
def SetTimetable():
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    f_timetable = open("ZoomJoiner/timetable.txt","w")
    for x in range(0,7):
        f_timetable.write("NewDay\n")
        print("=====" + weekdays[x] + "=====")
        try:
            numLessons = int(input("Enter number of lessons today: "))
        except:
            print("Invalid input! Try again")
        for y in range(numLessons):
            lessonName = input("Enter memorable name for lesson: ")
            lessonTime = input("Enter time of lesson (e.g. 1430): ")
            print("\n")
            lessonTime = str(lessonTime[0:2]) + ":" + str(lessonTime[2:4]) + ':00'
            #Run Validation to check if Lesson Name is correct
            line = lessonTime + ',' + lessonName
            f_timetable.write(line + '\n')
        if numLessons == 0:
            f_timetable.write('-\n')
    f_timetable.write("end")
    f_timetable.close()

    

        

    

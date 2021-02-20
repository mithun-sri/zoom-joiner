from zoom_joiner.test.addLesson import Lesson,AddLesson


def Initialise():
    try:
        f_codes = open("ZoomJoiner/codes.txt","a")
        f_codes.close()
    except:
        f_codes = open("ZoomJoiner/codes.txt","w")
        f_codes.close()
    
    numLessons = int(input("Enter the number of unique lessons you have: "))
    for x in range(numLessons):
        message = 'Enter a memorable name for lesson ' + str(x+1) + ' : '
        lessonName = input(message)
        message = 'Enter the zoom link for this lesson: '
        lessonLink = input(message)
        lesson = Lesson(lessonName,lessonLink)
        AddLesson(lesson)
        print("Lesson added.")

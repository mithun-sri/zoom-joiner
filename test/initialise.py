from zoom_joiner.test.add_lesson import add_lesson,Lesson


def Initialise():
    try:
        f_codes = open("zoom_joiner/codes.txt","a")
        f_codes.close()
    except:
        f_codes = open("zoom_joiner/codes.txt","w")
        f_codes.close()
    
    numLessons = int(input("Enter the number of unique lessons you have: "))
    for x in range(numLessons):
        message = 'Enter a memorable name for lesson ' + str(x+1) + ' : '
        lessonName = input(message)
        message = 'Enter the zoom link for this lesson: '
        lessonLink = input(message)
        lesson_obj = Lesson(lessonName,lessonLink)
        add_lesson(lesson_obj)
        print("Lesson added.")

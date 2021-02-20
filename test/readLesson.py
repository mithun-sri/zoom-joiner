from zoom_joiner.test.addLesson import Lesson

def ReadLessons():
    Lessons = []
    f_codes = open("ZoomJoiner/codes.txt","r")
    for line in f_codes:
        lessonDetails = line[0:-1].split(',')
        lesson = {
            lessonDetails[0]:lessonDetails[1]
        }
        Lessons.append(lesson)
    return Lessons




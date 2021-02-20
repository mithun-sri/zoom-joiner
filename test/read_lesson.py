from zoom_joiner.test.add_lesson import Lesson

def ReadLessons():
    Lessons = []
    f_codes = open("zoom_joiner/codes.txt","r")
    for line in f_codes:
        lessonDetails = line[0:-1].split(',')
        lesson = {
            lessonDetails[0]:lessonDetails[1]
        }
        Lessons.append(lesson)
    return Lessons




class Lesson:
    def __init__(self,lessonName,lessonLink):
        self.lessonName = lessonName
        self.lessonLink = lessonLink
    
    def get_lesson(self):
        return self.lessonName,self.lessonLink

def AddLesson(lesson):
    #Declares variable line which is to be appended into Codes.txt
    line = lesson.lessonName + ',' + lesson.lessonLink
    #Opens the file Codes.txt using f_codes
    f_codes = open("ZoomJoiner/codes.txt","a")
    f_codes.write(line+'\n')
    #Closes the file f_codes
    f_codes.close()
    

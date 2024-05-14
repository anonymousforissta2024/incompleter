#Source: https://stackoverflow.com/questions/53689831/exception-in-tkinter-callback-with-typeerror
from Tkinter import *
import tkMessageBox
course = list()

class Course:

    course = list()
    def __init__(self, longName, shortName, professor):
        self.longName = longName
        self.shortName = shortName
        self.professor = professor

    @staticmethod
    def importCourses():
        n=0
        course[:] = []
        with open('Courses.txt', 'r') as f:
            for line in f:
                if line == '\n':
                    continue
                longName, shortName, professor = line.rstrip("\n\r").split('-')
                course.append(Course(longName, shortName, professor))
                n=n+1
    @classmethod
    def createCourse(cls, newLongName, newShortName, newProfessor):
        with open('Courses.txt', 'r') as g:
            lines = g.readlines()
        with open('Courses.txt', 'a') as f:
            for line in lines:
                if ('-' + newShortName + '-') in line:
                    tkMessageBox.showinfo("Oops!", "There is already a Course with the name " + newShortName + '.')
                    return
            f.write(newLongName + '-' + newShortName + '-' + newProfessor)
        Course.importCourses()
    @staticmethod

    def createCourseEntry(self):
        createCourseEntryWindow = Toplevel(self)
        newCourseSNameLabel = Label(createCourseEntryWindow, text="Course Short Name:")
        newCourseSNameLabel.grid(row=0,column=0)
        newCourseLNameLabel = Label(createCourseEntryWindow, text="Course Long Name:")
        newCourseLNameLabel.grid(row=1,column=0)
        newCourseProfessorLabel = Label(createCourseEntryWindow, text="Course Professor:")
        newCourseProfessorLabel.grid(row=2,column=0)
        newCourseSNameEntry = Entry(createCourseEntryWindow)
        newCourseSNameEntry.grid(row=0,column=1)
        newCourseLNameEntry = Entry(createCourseEntryWindow)
        newCourseLNameEntry.grid(row=1,column=1)
        newCourseProfessorEntry = Entry(createCourseEntryWindow)
        newCourseProfessorEntry.grid(row=2,column=1)

        createNewCourseButton = Button(createCourseEntryWindow, text="Create", 
                      command=Course.createCourse(newCourseSNameEntry.get(),newCourseLNameEntry.get(),newCourseProfessorEntry.get()))
        createNewCourseButton.grid(row=3,column=0)
        cancelCreation = Button(createCourseEntryWindow, text="Cancel", command=lambda win=top: win.destroy())
        cancelCreation.grid(row=3,column=1)

    def deleteCourse(deleteShortName):
        with open('Courses.txt', 'r') as f:
            lines = f.readlines()
        with open('Courses.txt', 'w') as g:
            for line in lines:
                if ('-'+deleteShortName+'-') not in line:
                    g.write(line)
        Course.importCourses()

    def deleteCourseEntry(self):
        deleteCourseEntryWindow = TopLevel(self)
        deleteCourseLabel = Label(deleteCourseEntryWindow, text="Course Short Name:")
        deleteCourseLabel.grid(row=0, column=0)
        deleteCourseSNameEntry = Entry(deleteCourseEntryWindow)
        deleteCourseSNameEntry.grid(row=0,column=1)

        deleteCourseButton = Button(deleteCourseEntryWindow, text="Delete", 
                      command=Course.deleteCourse(deleteCourseSNameEntry.get()))
        deleteCourseButton.grid(row=1,column=0)
        cancelDeletion = Button(deleteCourseEntryWindow, text="Cancel", command=lambda win=top: win.destroy())
        cancelDeletion.grid(row=1,column=1)


Course.importCourses()
# Course.deleteCourse('LIT2380')
#Course.createCourse('Literature by Women','LIT2380','Alexandra Asbille')

root = Tk()

createCourseWindowButton = Button(root, text= 'Create Course', relief='solid', command=Course.createCourseEntry)
createCourseWindowButton.grid(row=0, column=0)
deleteCourseWindowButton = Button(root, text= 'Delete Course', relief='solid', command=Course.deleteCourseEntry)
deleteCourseWindowButton.grid(row=0, column=1)

courseSNameLabels = list()
courseLNameLabels = list()
courseProfessorLabels = list()

for x in range(0,len(course)):
    courseSNameLabels.append(Label(root, text= course[x].shortName, relief='solid'))
for x in range(0,len(course)):
    courseLNameLabels.append(Label(root, text= course[x].longName, relief='solid'))
for x in range(0,len(course)):
    courseProfessorLabels.append(Label(root, text= course[x].professor, relief='solid'))

m=1
for y in courseSNameLabels:
    y.grid(row=m)
    m=m+1
m=1
for y in courseLNameLabels:
    y.grid(row=m, column=1)
    m=m+1
m=1
for y in courseProfessorLabels:
    y.grid(row=m, column=2)
    m=m+1
root.mainloop()
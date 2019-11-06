class LinkedList:
    def __init__(self):
        self.head = None

    def addAsLast(self, node):
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while (tmp.next != None):
                tmp = tmp.next
            tmp.next = node

    def find(self, data):
        tmp = self.head
        while tmp != None:
            if tmp.isEqual(data):
                return tmp
            tmp = tmp.next
        return None

class Assignment:
    def __init__(self, title, deadline, percent):
        self.title = title
        self.deadline = deadline
        self.percent = percent
        self.grade = 0
        self.next = None

    def isEqual(self, title):
        return self.title == title

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.percent) + ": " + str(self.grade)

    def addGrade(self, grade):
        self.grade = grade

    def getActualGrade(self):
        return self.grade

    def getCalculatedGrade(self):
        return self.grade * self.percent/100

class Course:
    def __init__(self, ID):
        self.ID = ID
        self.assignments = LinkedList()
        self.next = None

    def isEqual(self, ID):
        return self.ID == ID

    def __str__(self):
        return self.ID

    def addAssignment(self, title, deadline, percent):
        assignment = Assignment(title, deadline, percent)
        self.assignments.addAsLast(assignment)

    def getAssignment(self, title):
        return self.assignments.find(title)


    def addGrade(self, title, grade):
        assignment = self.getAssignment(title)
        if (assignment != None):
            assignment.addGrade(grade)
        else:
            print("The Assignment", title, "doesn't exist for the student")

    def getGrade(self):
        grade = 0
        tmp = self.assignments.head
        while tmp != None:
            grade = grade + tmp.getCalculatedGrade()
            tmp = tmp.next
        return grade




class Student:
    def __init__(self, fName, lName, ID):
        self.fName = fName
        self.lName = lName
        self.ID = ID
        self.courses = LinkedList()

    def __str__(self):
        return self.getFullName() + ": " + self.ID


    def getFullName(self):
        return self.fName + " " + self.lName

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.addAsLast(course)

    def addAssignment(self, cID, title, deadline, percent):
        course = self.getCourse(cID)
        if (course != None):
            course.addAssignment(title, deadline, percent)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getCourse(self, ID):
        return self.courses.find(ID)

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self, cID, title, grade):
        course = self.getCourse(cID)
        if (course != None):
            course.addGrade(title, grade)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getCourseGrade(self, cID):
        course = self.getCourse(cID)
        return course.getGrade()



def main():
    my_student = Student("Arthur", "Sargsyan", "AUA234")
    print(my_student)

    #Adding Courses
    my_student.addCourse("ENGS115")

    print(my_student.getCourse("ENGS115"))
    print(my_student.getCourse("ENGS103"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Stack", "2019-10-31", 30)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))
    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Queue", "2019-11-05", 40)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    #adding Grades
    my_student.addGrade("ENGS115", "Implement Browser History using Stack", 90)
    my_student.addGrade("ENGS115", "Implement Browser History using Queue", 50)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    print(my_student.getCourseGrade("ENGS115"))
    # my_student.getAssignmentGrade("ENGS115", "Implement Browser History using Stack")
    # my_student.getAssignmentCalculatedGrade("ENGS115", "Implement Browser History using Stack")

main()
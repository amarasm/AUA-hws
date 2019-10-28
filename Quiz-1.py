class Student:
    def __init__(self, stName, stLastName):
        self.stName = stName
        self.stLastName = stLastName


class Assignment:
    def __init__(self, assignment, deadline, grade):
        self.assignment = assignment
        self.deadline = deadline
        self.grade = grade


    def assignmentAppend(self):
        list = []
        assignment = {"name:", self.assignment, "deadline:", self.deadline, "grade:", self.grade}
        list.append(assignment)
        return list

class Courses:
    def __init__(self):
        self.courses = []

    def courseAppend(self, course):
        courseList = self.courses.append(course)
        print((", ").join(courseList))







def main():

    student = Student("Amaras", "Mehrabi")
    course = Courses()
    course1 = course.courseAppend("ENG115")
    course2 = course.courseAppend("FND103")
    course3 = course.courseAppend("ENG123")
    course4 = course.courseAppend("ENG124")
    print("Assignments for", course1, "are:")





main()
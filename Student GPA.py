class Student:
    def __init__(self, name = None, gpa = None):
        self.name = name
        self.gpa = gpa
        self.next = None

class GPA:
    def __init__(self):
        self.__head = None

    def setHead(self, newName, newGPA):
        self.__head = Student(newName, newGPA)

    def display(self):
        printName = self.__head
        while printName is not None:
            print(printName.name, printName.gpa)
            printName = printName.next
        print("***************")

    def append(self, newName, newGPA):
        temp = self.__head
        while temp.next is not None:
            temp = temp.next

        newStudent = Student(newName, newGPA)
        temp.next = newStudent

    def highGPA(self):
        temp = self.__head
        while temp is not None:
            if temp.gpa >= 3.4:
                print(temp.name)
                temp = temp.next
            else:
                temp = temp.next
        print("^^ The students with high GPA ^^")

    def orderedGPA(self):
        temp = self.__head
        curFix = temp.gpa
        curEl = temp.next.gpa
        while temp is not None:
            if curFix > curEl:
                smth = curFix
                curFix = curEl
                temp.next.next.gpa = smth
            else:
                curEl = temp.next.next.gpa


def main():

    student = GPA()

    student.setHead("Liyoda", 3.7)

    student.append("Tiledia", 3.2)
    student.append("Predita", 4.0)
    student.append("Lina", 2.8)
    student.append("Nare", 2.7)
    student.append("Amaras", 3.4)
    student.display()

    student.highGPA()
    student.orderedGPA()


main()



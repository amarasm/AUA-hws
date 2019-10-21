class Student:
    def __init__(self, name = None, gpa = None):
        self.name = name
        self.gpa = gpa
        self.next = None

class GPA:
    def __init__(self):
        self.head = None

    def setHead(self, newName, newGPA):
        self.head = Student(newName, newGPA)

    def display(self):
        printName = self.head
        while printName is not None:
            print(printName.name, printName.gpa)
            printName = printName.next
        print("***************")

    def append(self, newName, newGPA):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        newStudent = Student(newName, newGPA)
        temp.next = newStudent


    def highGPA(self):
        array = []
        temp = self.head
        while True:
            if  temp.gpa >= 3.4:
                data = self.head
                array.append(data)
            else:
                break

    def GPAlist(self):
        array = []
        temp = self.head
        while True:
            if temp.next is not None:
                newData = self.head[1]
                array.append(newData)
            else:
                newData = self.head[1]
                array.append(newData)
                break
        return array


    def merge(self, a, b):
        c = []
        while len(a) != 0 and len(b) != 0 :
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])

        if len(a) == 0:
            c += b
        else:
            c += a
        return c


    def mergeSort(self, array):
        if len(array) == 0 or len(array) == 1:
            return array
        else:
            middle = int(len(array)/2)
            a = mergeSort(array[:middle])
            b = mergeSort(array[middle:])
            c = merge(a, b)
            print(c)
            return c


def main():

    student = GPA()

    student.setHead("Liyoda", 3.7)

    student.append("Tiledia", 3.2)
    student.append("Predita", 4.0)
    student.append("Lina", 2.8)
    student.append("Nare", 2.7)
    student.append("Amaras", 3.4)
    student.display()
    print(student.highGPA())
    array = student.GPAlist()
    print(student.mergeSort(array))



main()



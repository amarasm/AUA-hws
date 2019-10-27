class List:

    def __init__(self, link = None):
        self.link = link
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False



    def push(self, newLink):
        if self.__head == None:
            self.__head = List(newLink)

        else:
            newData = List(newLink)
            newData.next = self.__head
            self.__head = newData

    def back(self):
        if self.isEmpty():
            return None
        else:
            poppedData = self.__head
            self.__head = self.__head.next
            global frw
            frw = poppedData
            poppedData.next = None
            return poppedData.link


    def open(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.link

    def display(self):
        printval = self.__head
        if self.isEmpty():
            print("Stack is empty")
        else:
            while printval is not None:
                print(printval.link)
                printval = printval.next


    def forward(self):
        temp = self.__head
        if temp.next is not None:
            print(frw.link)
        else:
            print("No Data")



def main():
    list = Stack()


    list.push("aua.am")
    list.push("im.aua.am")
    list.push("google.com")
    print("\nThe initial list is:")
    list.display()
    print("\nTop element is:", list.open())
    print("\nWe are now going one step back")
    list.back()
    print("Displaying the list:")
    list.display()
    print("\nAnd the top element is:", list.open())
    list.forward()
    print("\nGoing one step forward, the top element is:", list.open())

    list.back()
    print("\nAgain going one step back. Top element:", list.open())
    print("\nNow we display what we have in our list")
    list.display()
    print("\nTop element is", list.open())


main()







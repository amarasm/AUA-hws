class Grade:
    min = 0
    max = 100

    def __init__(self, mark=-1):
        if (mark == -1):
            self.mark = Grade.askUserInput()
        else:
            self.mark = mark

    @classmethod
    def askUserInput(cls):
        return int(input("please insert the grade"))

    def display(self):
        if (self.isValid()):
            print(self.mark)
        else:
            print("invalid mark")

    def isValid(self):
        return Grade.min <= self.mark and self.mark <= Grade.max

def main():
    gr1 = Grade(85)
    gr1.display()


    gr2 = Grade(185)
    gr2.display()


    gr3 = Grade()
    gr3.display()

main()
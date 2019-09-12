class Classroom:

    def __init__(self, seats, classnumber, eastWestM):
        self.seats = seats
        self.classnumber = classnumber
        self.eastWestM = eastWestM
        self.schedule = []

    def LocateTheClass(self):
        print("the location of the class is", self.classnumber + self.eastWestM)

    def classIsFree(self, start, end):
        isFree = True
        for slot in self.schedule:
            if (slot["start"] >= start and slot["end"] <= start) or (slot["start"] <= end and slot["end"] <= end):
                continue
            else:
                isFree = False
                break
        return isFree


    def bookClassRoom(self, start, end):
        if (self.classIsFree(start, end)):
            Timeslot = {"start":start, "end":end}
            self.schedule.append(Timeslot)
            return True
        else:
            return False



def main():
    myclass = Classroom(100, "208", "East")


    start = input("Please enter the start time")
    end = input("Please enter the end time")
   

    while True:
        if myclass.bookClassRoom(start, end) == False:
            print("This classroom is booked for the interval you have entered. Please choose another interval")
            start = input("Please enter the start time")
            end = input("Please enter the end time")
        else:
            print(myclass.schedule)
            break


main()

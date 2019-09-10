class Classroom:

    def __init__(self, seats, classnumber, eastWestM):
        self.seats = seats
        self.classnumber = classnumber
        self.eastWestM = eastWestM
        self.schedule = []

    def LocateTheClass(self):
        print("the location of the class is", self.classnumber + self.eastWestM)

    def classIsFree(self, start, end):
        if (self.schedule.cl1[0] >= start and self.schedule.cl1[0] >= start) or (self.schedule.cl1[1] <= end and self.schdule.cl1[1] <= end):
            return False
        else:
            return True

    def bookClassRoom(self, start, end):
        if (self.classIsFree(start, end)):
            Timeslot = {"start":start, "end":end}
            self.schedule.append(Timeslot)
            return True
        else:
            return False



def main():
    myclass = Classroom(100, "208", "East")
    cl1 = Classroom(100, "208", "East")

    start = input("Please enter the start time")
    end = input("Please enter the end time")
    cl1.schedule.append({"start": 1235, "end":1467})

    while not(myclass.bookClassRoom(start, end)):
        print("This classroom is booked for the interval you have entered. Please choose another interval")
        start = input("Please enter the start time")
        end = input("Please enter the end time")

    print(myclass.schedule)


main()
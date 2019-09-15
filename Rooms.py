class Room:

    rooms = {}

    def __init__(self, roomID, capacity):
        self.capacity = capacity
        self.roomID = roomID
        self.schedule = []
        Room.rooms[roomID] = self
        print(Room.rooms)

    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break

        return is_free

    def Reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False


    @classmethod
    def getAvailableRooms(cls):
        ids = []
        for key in cls.rooms:
            ids.append(key)
        return str.join(",", ids)


    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.rooms.keys():
            return cls.rooms[ID]
        print("the room cannot be found")
        return False


    @classmethod
    def getcurrentscheduleofAllRooms(cls):
        for key in cls.rooms:
            currRoom = cls.rooms[key]
            print(currRoom.roomID, ' :')
            print("capacity: ", currRoom.capacity)
            print("schedule: ", currRoom.schedule)


    @staticmethod
    def isValidSlot(start, end):
        return start < end




class Classroom(Room):

    def __init__(self, roomID, capacity):
        super().__init__(roomID, capacity)



class Office(Room):
    def __init__(self, roomID, capacity, instructor):
        super().__init__(roomID, capacity)
        self.instructor = instructor



def mainClassroom():
    Classroom("208E PAB", 60)
    Classroom("314W PAB", 30)
    Classroom("114W PAB", 45)
    Classroom("118W PAB", 50)

    print("Hello, here you can reserve a classroom. Available IDs are:\n", Classroom.getAvailableRooms())

    while True:
        classroomID = input("Please select a room ID from above")
        currClassroom = Classroom.getRoomById(classroomID)
        if currClassroom == False:
            break
        start = int(input("Please insert the starting time"))
        end = int(input("Please insert the ending time"))

        if (Classroom.isValidSlot(start, end)):
            if currClassroom.isFree(start, end) == False:
                print("Not available for ", currClassroom.roomID)
            else:
                currClassroom.Reserve(start, end)
                print("You just reserved the classroom", currClassroom.roomID, " from ", start, " to ", end)

                print(currClassroom.schedule)
        else:
            print("The slot is invalid")


def mainOffice():
    Office("209E PAB", 3, "Satenik Mnatsakanyan")
    Office("115E PAB", 2, "Lilianna Edilian")
    Office("001 PAB", 3, "Maryam Mikhaylova")

    print("Hello, here you can reserve an Office. Available IDs are:\n", Office.getAvailableRooms())

    while True:
        OfficeID = input("Please select a room ID from above")
        currOffice = Office.getRoomById(OfficeID)
        if currOffice == False:
            break

        start = int(input("Please insert the starting time"))
        end = int(input("Please insert the ending time"))

        if (Office.isValidSlot(start, end)):
            if currOffice.isFree(start, end) == False:
                print("Not available for ", currOffice.roomID)
            else:
                currOffice.Reserve(start, end)
                print("You just reserved the classroom", currOffice.roomID, " from ", start, " to ", end)
                print(currOffice.schedule)
        else:
            print("The slot is invalid")


def main():
    while True:
        Choice = input("dear user, Do you want to reserve an office or a classroom? type yes or no")
        if Choice == "yes":
            while True:
                RoomChosen = input("Dear user if you want to reserve a classroom input 1, and input 2 to reserve an Office: ")
                if RoomChosen == '1':
                    mainClassroom()
                    break
                if RoomChosen == '2':
                    mainOffice()
                    break
                else:
                    print("Please try again, input the integers mentioned above: ")
        elif Choice == "no":
            print("Okay! If you changed your mind come back!")
            break
        else:
            print("Please type either 'yes' or 'no'.")
            break

main()
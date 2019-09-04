class Student:
    Participation = 0.10
    Homework = 0.30
    Quizzes = 0.20
    FinalProject = 0.40

    def __init__(self, ID, firstName, lastName, phone, gender, birthdate, participation, homework, quizzes, finalProject):
        self.ID = ID
        self.fullName = firstName + " " + lastName
        self.email = firstName + "." + lastName + "@aua.am"
        self.phone = phone
        self.gender = gender
        self.birthdate = birthdate
        self.participation = participation
        self.homework = homework
        self.quizzes = quizzes
        self.finalProject = finalProject


    def getPersonalInfo(self):
        print(self.ID)
        print(self.fullName)
        print(self.email)
        print(self.phone)
        print(self.gender)
        print(self.birthdate)
        print("----------------------")


    def getCurrentGrade(self):
        finalParticipation = float(self.Participation * self.participation)
        finalHomework = float(self.Homework * self.homework)
        finalQuizzes = float(self.Quizzes * self.quizzes)
        finalProject = float(self.FinalProject * self.finalProject)
        finalGrade = float(finalParticipation + finalHomework + finalQuizzes + finalProject)
        print(finalGrade)



def main():
    st1 = Student("AUA123", "User1", "no1", "123456", "M", "01/01/2019", 100, 90, 92, 100)
    st2 = Student("AUA123", "User2", "no2", "654321", "F", "01/01/2018", 87, 93, 100, 98)

    st1.getPersonalInfo()
    st2.getPersonalInfo()
    st1.getCurrentGrade()
    st2.getCurrentGrade()



main()

class Task:

    def __init__(self, task, date, importanceLevel):
        self.task = task
        self.date = date
        self.importanceLevel = importanceLevel
        self.importance = {}


    def returnTask(self):
        return self.task

    def importanceArray(self):
        Array = {self.Task: self.importanceLevel}
        self.importance.update(Array)
        return Array


    def importanceOfTask(self):
        array = [self.importanceLevel]
        self.importance.update(array)
        return array


class TaskManager:

    def __init__(self):
        self.Tasks = []

    def addTask(self, new):
        self.new = new
        Task = self.new.returnTask()
        self.Tasks.append(Task)

    def printAllTasks(self):
        print("All the tasks that you have are")
        print(self.Tasks, sep = ",")

    def printTheMostImportantTask(self):
        important = self.new.importance
        itemMaxValue = max(self.printAllTasks(), important)

        print("Key with maximum value in dictionary: ", itemMaxValue[0])



def main():

    auaTasks = TaskManager()
    personalTasks = TaskManager()

    t = Task("Calculus HW", "10/10/19", 8)
    auaTasks.addTask(t)

    t = Task("Get ready for Midterms", "26/10/19", 5)
    auaTasks.addTask(t)

    t = Task("Pay cellphone Bill", "22/10/19", 2)
    personalTasks.addTask(t)

    t = Task("Sister's Birthday gift", "22/10/19", 10)
    personalTasks.addTask(t)

    auaTasks.printAllTasks()

    personalTasks.printTheMostImportantTask()

main()

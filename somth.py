def ArrayRange():
    while True:
        n = input("Please insert the range of your array")
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("Please insert numbers")
    return n


def createASet(n):
    set = []
    for i in range(n):
        while True:
            createSet = input("Input a number you want to have in your set")
            if createSet.isnumeric():
                createSet = int(createSet)
                set.append(createSet)
                print(set)
                break
            else:
                print("Please insert numbers")


def sum(set):
    sum = 0
    for i in set:
        sum = sum + i
    return sum


def main():
    Array = ArrayRange()
    CreatedSet = createASet(Array)
    Sum = sum(CreatedSet)

main()


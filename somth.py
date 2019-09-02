def ArrayRange():
    while True:
        n = input("Please insert the range of your array")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("Please insert integers")
    return n


def createASet(n):
    set = []
    for i in range(n):
        while True:
            createSet = input("Input a number you want to have in your set")
            if createSet.isnumeric():
                createSet = int(createSet)
                set.append(createSet)
                break
            else:
                print("Please insert numbers")
    print (set)
    return set


def sum(set):
    sum = 0
    List = []
    for i in set:
        sum = sum + i
        List.append(sum)
    print (List)
    return List


def main():
    Array = ArrayRange()
    CreatedSet = createASet(Array)
    Sum = sum(CreatedSet)

main()

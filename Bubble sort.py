
def bubbleSortingTheArray():
    array = [6, 2, 9, 7, 4, 8]
    print(array)
    for i in range(len(array)):
        i = 0
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)


bubbleSortingTheArray()


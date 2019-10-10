
def sortingTheArray():
    array = [5, 3, 8, 7, 1, 4]
    print(array)
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum] > array[j]:
                minimum = j
        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]
    print(array)


sortingTheArray()




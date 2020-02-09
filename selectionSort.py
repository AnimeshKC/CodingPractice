import random

def selectionSort(arr):
    arrLen = len(arr)
    maxIndex = arrLen -1
    for i in range(0, arrLen):
        minIndex = i
        #j points from i until the end of the array
        j = i
        while j < maxIndex:
            j += 1
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def main():
    minInt = 0
    maxInt = 10
    numRange = 15
    #randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    randomList = [7, 11, 89, 2, 56, 12, 8, 10, 0, 55, 23]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    selectionSort(randomList)
    print(randomList)
main()


import random

#function median of three will only get called if length is at least 2
#median of first, middle, and last element of list becomes the last element of the list
def medianOfThree(arr, lowIndex, highIndex):
    lowValue = arr[lowIndex]
    highValue = arr[highIndex]
    midIndex = (lowIndex + highIndex) //2
    midValue = arr[midIndex]
    if arr[highIndex] < arr[lowIndex]:
        arr[lowIndex], arr[highIndex] = arr[highIndex], arr[lowIndex]
    if arr[midIndex] < arr[lowIndex]:
        arr[midIndex], arr[lowIndex] = arr[lowIndex], arr[midIndex]
    if arr[highIndex] < arr[midIndex]:
        arr[highIndex], arr[midIndex] = arr[midIndex], arr[highIndex]
    return midIndex

def partition(arr, lowIndex, highIndex):
    pivotIndex = medianOfThree(arr, lowIndex, highIndex)
    pivot = arr[pivotIndex]
    #i represents the index from which all elements before it and in it are less than the pivot
    i = lowIndex -1 
    for j in range(lowIndex, highIndex):
        if arr[j] < pivot: #what j with the value in i
            i += 1
            #if the pivotIndex is to swap, then update the pivotIndex
            if i == pivotIndex:
                pivotIndex = j
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i] 
    return i
def quickSort(arr, lowIndex, highIndex):
    if lowIndex < highIndex:
        partitionIndex = partition(arr, lowIndex, highIndex)
        quickSort(arr, lowIndex, partitionIndex -1)
        quickSort(arr, partitionIndex + 1, highIndex)

def main():
    minInt = 17
    maxInt = 255
    numRange = 25
    randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    #randomList = [7, 11, 89, 2, 56, 12, 8, 10, 0, 55, 23]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    quickSort(randomList, 0, len(randomList)-1)
    print(randomList)

main()
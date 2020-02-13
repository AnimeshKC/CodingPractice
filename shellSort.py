import random
#Identify and resolve sorting error
def shellSort(arr):
    arrSize = len(arr)
    #Using Knuth's increments  1, 4, 13, 40, ...
    increment = 1
    while increment < arrSize//3:
        increment = 3 * increment + 1
    while increment >= 1:
        for i in range(increment, arrSize):
            j = i
            newIndex = j - increment
            newValue = arr[newIndex]
            currentValue = arr[j]
            while j >= increment and currentValue < newValue:
                swapIndex = j - increment
                arr[j], arr[swapIndex] = arr[swapIndex], arr[j]
                j = j - increment
        increment = increment // 3

def main():
    minInt = 0
    maxInt = 255
    numRange = 50
    randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    #randomList = [7, 11, 89, 2, 56, 12, 8, 10, 0, 55, 23]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    shellSort(randomList)
    isSorted = all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1))
    print(isSorted)
    print(randomList)

main()
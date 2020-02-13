import random
def shellSort(arr):
    arrSize = len(arr)
    #Using Knuth's increments  1, 4, 13, 40, ...
    increment = 1
    while increment < arrSize//3:
        increment = 3 * increment + 1
    while increment >= 1:
        for i in range(increment, arrSize):
            j = i
            while j >= increment and arr[j] < arr[j - increment]:
                arr[j], arr[j - increment] = arr[j - increment], arr[j]
                j = j - increment
        increment = increment // 3

def main():
    minInt = 0
    maxInt = 255
    numRange = 14
    #randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    randomList = [111, 165, 149, 254, 232, 100, 181, 118, 250, 229, 88, 208, 109, 254, 17]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    shellSort(randomList)
    isSorted = all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1))
    print(isSorted)
    print(randomList)

main()
import random

def insertionSort(arr):
    assert len(arr) > 1
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i
        while j > 0 and currentVal < arr[j-1]:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = currentVal


def main():
    minInt = 0
    maxInt = 10
    numRange = 15
    #randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    randomList = [7, 11, 89, 2, 56, 12, 8, 10, 0, 55, 23]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    insertionSort(randomList)
    print(randomList)
main()
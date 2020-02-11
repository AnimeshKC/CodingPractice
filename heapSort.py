import random

def heapify(arr, heapSize, root):
    largest = root
    leftChild = 2 * root + 1
    rightChild = 2 * root + 2
    if leftChild < heapSize and arr[largest] < arr[leftChild]:
        largest = leftChild
    if rightChild < heapSize and arr[largest] < arr[rightChild]:
        largest = rightChild
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, heapSize, largest)

def heapSort(arr):
    arrSize = len(arr)
    for i in range(arrSize, -1, -1):
        root = i
        heapify(arr, arrSize, root)
    for i in range(arrSize-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    minInt = 0
    maxInt = 255
    numRange = 5000
    randomList = [random.randrange(minInt, maxInt) for i in range(numRange)]
    #randomList = [7, 11, 89, 2, 56, 12, 8, 10, 0, 55, 23]
    print("Before the sort: ")
    print(randomList)
    print("\n After the sort: ")
    heapSort(randomList)

    isSorted = all(randomList[i] <= randomList[i+1] for i in range(len(randomList)-1))
    print(isSorted)
    print(randomList)

main()
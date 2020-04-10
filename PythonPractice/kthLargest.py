
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
    for j in range(lowIndex, highIndex + 1):
        if arr[j] < pivot: #what j with the value in i
            i += 1
            #if the pivotIndex is to swap, then update the pivotIndex
            if i == pivotIndex:
                pivotIndex = j
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i] 
    return i

def kthLargest(arr, k):
    '''returns the kth smallest element in arr using quickselection'''
    n = len(arr)
    lowIndex = 0
    highIndex = n -1
    partitionIndex = partition(arr, lowIndex, highIndex)
    finalIndex = n - k
    while partitionIndex != finalIndex:
        if partitionIndex < finalIndex:
            lowIndex = partitionIndex + 1
        elif partitionIndex > finalIndex:
            highIndex = partitionIndex - 1
        partitionIndex = partition(arr, lowIndex, highIndex)
    return arr[partitionIndex]

def main():
    testArr = [3,2,1,5,6,4]
    k = 2
    answer = kthLargest(testArr, k)
    print(answer)
main()

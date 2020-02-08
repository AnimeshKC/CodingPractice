
def mergeSort(arr):
    #if list has more than 1 item
    if len(arr) > 1:
        mid = len(arr)//2
        leftList = arr[:mid]
        rightList = arr[mid:]
        mergeSort(leftList)
        mergeSort(rightList)

        leftIndex = rightIndex = arrayIndex = 0

        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex] < rightList[rightIndex]:
                arr[arrayIndex] = leftList[leftIndex]
                leftIndex +=1
            else:
                arr[arrayIndex] = rightList[rightIndex]
                rightIndex +=1
            arrayIndex += 1

        #for any elements left
        #Only one of the following should execute
        while leftIndex < len(leftList):
            arr[arrayIndex] = leftList[leftIndex]
            arrayIndex += 1
            leftIndex +=1 
        while rightIndex < len(rightList):
            arr[arrayIndex] = rightList[rightIndex]
            arrayIndex += 1
            rightIndex += 1

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


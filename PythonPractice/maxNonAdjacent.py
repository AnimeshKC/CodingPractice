
#Time complexity, for an array of n elements:
    #O(n) -> one pass of the array
#Space complexity:
    #O(1) -> needs only 3 extra variables to keep track of state

def maxNonAdjacent(arr):
    '''returns the maximum sum of non-adjacent numbers in an array using dynamic programming'''
    exclusiveMax = 0 #the maximum sum before the current number
    inclusiveMax = 0 #the maximum sum including the current number

    for num in arr:
        #This entire body could be done in one line 
        #with tuple unpacking,
        #but the implementation would be less intuitive
        
        previousMax = inclusiveMax #maximum before current iteration is the previous inclusive max
        
        #update the inclusive and exclusive max
        #By the nature of this inclusive max update, this function works for negative values as well
        inclusiveMax = max(previousMax, exclusiveMax + num) 
        
        exclusiveMax = previousMax #update exclusive max for the next iteration
    return inclusiveMax
def main():
    assert(maxNonAdjacent([30, 20, 10, 5]) == 40) #basic test 
    assert(maxNonAdjacent([4, 1, 1, 4, 2, 1]) == 9) #test for the case where multiple elements in a sequence are to be ignored
    assert(maxNonAdjacent([]) == 0) #test for empty array
    assert(maxNonAdjacent([15]) == 15) #test for array with one element
    assert(maxNonAdjacent([1, 2, 1, 6]) == 8) #test for not using the first element
    assert(maxNonAdjacent([-5, 1, 0, 10]) == 11) #For completeness, test an array with a negative number
    assert(maxNonAdjacent([-5, -1, -10]) == 0) #test that if all values are negative, none of them will be summed
    assert(maxNonAdjacent([-5, 1, -10]) == 1) #if all but one are negative, only that value is used
    print("All Tests have passed")

if __name__ == "__main__":
    main()

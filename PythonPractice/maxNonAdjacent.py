
def maxNonAdjacent(arr):
    '''returns the maximum sum of non-adjacent numbers using dynamic programming
    Time Complexity: O(N)
    Space Complexity: O(1)'''
    #[30, 20, 10, 5]
    exclusiveMax = 0 #represents the maximum sum before the current number
    inclusiveMax = 0 #represents the maximum sum including the current number

    for num in arr:
        previousMax = inclusiveMax #get maximum before this element
        #update the inclusive and exclusive max
        inclusiveMax = max(previousMax, exclusiveMax + num) 
        exclusiveMax = previousMax #update exclusive max to be the previous maximum
    return inclusiveMax

if __name__ == "__main__":
    assert(maxNonAdjacent([30, 20, 10, 5]) == 40) #simple test 
    assert(maxNonAdjacent([4, 1, 1, 4, 2, 1]) == 9) #test for not necessarily 2 apart
    assert(maxNonAdjacent([]) == 0) #test for empty array
    assert(maxNonAdjacent([15]) == 15) #test for array with one element
    assert(maxNonAdjacent([1, 2, 1, 6]) == 8) #test for not using the first element
    print("All Tests have passed")


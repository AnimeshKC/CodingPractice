def twoSum(arr, target):
    '''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    Exactly one solution without using the same index twice'''
    assert(len(arr) > 1)
    valDict = {}
    for i in range(len(arr)):
        currentVal = arr[i]
        complement = target - currentVal
        if currentVal in valDict:
            return [valDict[currentVal], i]
        else:
            valDict[complement] = i    
    #No solution found
    return False

#sanity test
testArr = [3, 5, 2, -4, 8, 11]
assert(twoSum(testArr, 8) == [0, 1])
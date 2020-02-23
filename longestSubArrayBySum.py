def findLongestSubArrayBySum(arr, targetSum):
    returnArr = [-1]
    if len(arr) == 0:
        return returnArr
    left = 0
    right = 0
    sum = 0

    while right < len(arr):
        sum += arr[right]
        while left < right and sum > targetSum:
            sum -= arr[left]
            left += 1
        
        if (sum == targetSum and len(returnArr) == 1) or (sum == targetSum and ((right - left) > (returnArr[1] - returnArr[0]))):
            returnArr = [left + 1, right + 1]
        right += 1
    return returnArr
print(findLongestSubArrayBySum([10, 5, 8, 2, 5, 0, 0, 0, 6, 7, 8, 9, 10], 15))
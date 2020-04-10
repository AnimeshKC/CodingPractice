def expandAroundCenter(s, left, right):
    while left >=0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    #left is one to the left of where it ends, so increment 1
    return s[left+1:right]
def longestPalindrome(s):
    for i in range(len(s)):
        center = expandAroundCenter(s, i, i)
        inBetween = expandAroundCenter(s, i, i+1)
        longestSub = max(longestSub, center, inBetween, key = len)
        return longestSub

testStr = "racecar"
print(longestPalindrome(testStr))
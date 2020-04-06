class Solution:
    def maxLength(self, arr):
        currentSize = 0
        #list has at least 1 element
        if len(arr) == 1:
            if self.uniquePair(arr[0], ""):
                currentSize = len(arr[0]) #maxSize is size of string if there's only one string
            return currentSize
        for i in range(len(arr)):
            if self.uniquePair(arr[0], ""):
                currentSize = self.findConcatenation(arr[i], i, arr, currentSize)
        return currentSize
    def findConcatenation(self, currentString, startIndex, arr, currentSize):
        if len(currentString) > currentSize:
            currentSize = len(currentString)
            return self.findConcatenation(currentString, startIndex, arr, currentSize)
        if (startIndex + 1) < len(arr):
            newString = arr[startIndex + 1]
            if self.uniquePair(currentString, newString):
                currentString = currentString + newString
                if len(currentString) > currentSize:
                    currentSize = len(currentString)
            return self.findConcatenation(currentString, startIndex + 1, arr, currentSize)
        return currentSize 
    def uniquePair(self, string1, string2):
        charSet = set()
        
        for c in string1:
            if c in charSet:
                return False
            else:
                charSet.add(c)
        for c2 in string2:
            if c2 in charSet:
                return False
            else:
                charSet.add(c2)
        return True

instance = Solution()
print(instance.maxLength(["a", "abc", "d", "de", "def"]))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        map = {}
        maxLen = start = 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start +1)
            map[s[i]] = i
        return maxLen

        
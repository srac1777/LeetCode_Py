from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        stringHsh = Counter(s)
        for i in range(len(s)):
            if stringHsh[s[i]] == 1:
                return i
        return -1
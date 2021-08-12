class Solution:
    def getIsPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        return False

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            return self.getIsPalindrome(x)

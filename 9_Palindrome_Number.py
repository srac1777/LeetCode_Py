class Solution:
    def getIsPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        return False
    
    def num_reverse(self, x):
        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x = int(x/10)
        return res
        
    def getIsPalindromeUsingNumbers(self, x):
        return x == self.num_reverse(x)

    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            return self.getIsPalindromeUsingNumbers(x)
        
    

class Solution:
    def findWords(self, words):
        top_row = self.construct_hash("qwertyuiop")
        middle_row = self.construct_hash("asdfghjkl")
        bottom_row = self.construct_hash("zxcvbnm")

        result = []

        for word in words:
            if word[0].lower() in top_row and self.check_row(word, top_row):
                result.append(word)
            elif word[0].lower() in middle_row and self.check_row(word, middle_row):
                result.append(word)
            elif self.check_row(word, bottom_row):
                result.append(word)

        return result

    def construct_hash(self, str):
        hsh = {}
        for letter in str:
            if letter in hsh:
                hsh[letter] += 1
            else:
                hsh[letter] = 1
        return hsh

    def check_row(self, word, row_hash):
        for letter in word:
            if letter.lower() not in row_hash:
                return False
        return True

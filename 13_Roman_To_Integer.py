class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = roman_map[s[0]]
        prev = s[0]

        for i in range(1, len(s)): # remember range second arg is exclusive
            if roman_map.get(s[i]) <= roman_map[prev]:
                total += roman_map[s[i]]
            else:
                total -= 2*roman_map[prev]
                total += roman_map[s[i]]
            prev = s[i]
        return total

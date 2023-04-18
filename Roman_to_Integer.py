class Solution(object):
    def romanToInt(self, s: str) -> int:
        #largest number to smallest number: added them up later on
        #smaller before larger: subtract smaller

        roman = {"I": 1, "V": 5, "X": 10, 
        "L": 50, "C": 100, "D":500, "M": 1000 }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s):
                
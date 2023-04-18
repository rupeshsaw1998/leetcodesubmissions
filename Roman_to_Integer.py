class Solution(object):
    def romanToInt(self, s: str) -> int:
    #-> marks the return function annotation indicating the function returns an int.
        
        #largest number to smallest number: added them up later on
        #smaller before larger: subtract smaller

        # s is the input from the user

        roman = {"I": 1, "V": 5, "X": 10, 
        "L": 50, "C": 100, "D":500, "M": 1000 }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += romans[s[i]]

        return res

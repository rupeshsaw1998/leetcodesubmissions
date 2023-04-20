#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            #checking if the length is same
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            #index i is gonna be used for both the strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            #counting the occurence of each character in the string
            #get(a, 0) will set initial value as zero if there is no occurence of that character previouslwly
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                #here we are comparing count of character and c is the key
                return False

        return True

#second solution

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True

        else:
            return False
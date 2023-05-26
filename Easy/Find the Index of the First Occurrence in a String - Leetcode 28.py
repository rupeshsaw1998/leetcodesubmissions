class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #if we have an empty string we return 0
        if needle == "":
            return 0
        
        #here we're starting to check the haystack by starting at ever yposition exceot the last last one
        for i in range(len(needle) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
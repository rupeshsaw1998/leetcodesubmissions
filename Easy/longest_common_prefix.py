#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".





class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            #iterating through every index
            for s in strs:
                #iterating through every string 
                if i == len(s) or s[i] != strs[0][i]:
                    #condition 1: checks if the word is finished 
                    #condition 2: checking if first character is same in every index/ word in the list
                    return res

            res +=strs[0][i]

        return res
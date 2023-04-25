#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list) #mapping count of char

        for s in strs:
            count = [0] * 26
            #counting number of characters a....z

            for c in s:
                count[ord(c) - ord("a")] += 1
                #mapping a to 0 and z to 25. here we subtracted the ascii value i.e. a-a = 0 and then incrementing by 1

            res[tuple(count)].append(s)
            # we are grouping all the anagrams using count
            #res[count].append(s) we changed this to a tuple as lists cannot be keys

        return res.values()

        
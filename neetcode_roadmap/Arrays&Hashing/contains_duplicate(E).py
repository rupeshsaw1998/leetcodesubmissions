#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rep = {}
        for i in range(len(nums)):
            rep[nums[i]] = 1 + rep.get(nums[i], 0)
        
        print(rep)

        for c in rep:
            if rep[c] != 1:
                return True
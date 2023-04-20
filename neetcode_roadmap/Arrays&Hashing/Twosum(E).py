#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        #it's a hashmap
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                #checking if the difference is already in the hashmap
                return [prevMap[diff], i]
                #if it is the it'll return indexes
            prevMap[n] = i
        return
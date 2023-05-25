class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #left pointer is initialized at 1 as 0th position is not going to change
        l = 1

        #we're initializing right pointer as 1
        for r in range(1, len(nums)):
            #checking if the value we see is new value by comparing it with previous value
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l
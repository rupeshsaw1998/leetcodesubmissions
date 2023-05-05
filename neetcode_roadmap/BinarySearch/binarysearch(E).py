class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0 , len(nums) - 1
         #taking two extreme ends of the list and dividing and comparing them

        while l <= r:
             #to keep checking if the pointer is out of values to check
             m = l + ((r - l) // 2)

             if nums[m] > target:
                r = m - 1
            #we are looking to the left or shgrinking our criteria
             elif nums[m] < target:
                l = m + 1
            #we are looking to the right or expanding our criteria
             else:
                 return m
            # here we found the value and returning the position of the target

        return -1
        #if we don't find the value
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        #left and right pointers
        res = r

        while l <= r:
            k = (l + r)//2
            #k is the midpoint
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                #to calculate the number of hours it took to eat

            if hours <= h:
                res = min(res, k)
                r = k - 1
                #checking if the obtained hours is less than h to find, if it is the decreasing by 1
            else:
                l = k + 1
                #increasing the value of k as hours is less than h(the one we found out through loop)

            
        return res
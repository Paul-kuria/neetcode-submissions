from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ''' [25, 10, 23, 4] 
            -> 4
            - k is btwn 1 and max(piles)
        '''

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours_to_eat = 0

            hours_to_eat = sum([ceil(p/k) for p in piles])

            if hours_to_eat <= h:
                # Current rate too fast
                res = min(res, k)
                r = k - 1
            elif hours_to_eat > h:
                # Current rate too slow
                l = k + 1

        return res



        

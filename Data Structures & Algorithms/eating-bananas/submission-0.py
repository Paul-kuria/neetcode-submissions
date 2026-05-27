class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Check what ranges still fall within our target h..
        l = 1
        r = max(piles)
        res = r # Max value

        while l <= r:
            # Mid point of speed
            k = (l + r) // 2
            hours = 0
            
            # Calculate total hours
            for p in piles:
                hours +=  math.ceil(p / k)
                

            # If hours are more than h
            if hours <= h:
                print(res, k)
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
                
        return res
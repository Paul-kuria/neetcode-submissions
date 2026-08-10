class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while l<r:
            max_height = min(heights[l], heights[r])
            max_area = max_height * (r-l)
            res = max(res, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
        

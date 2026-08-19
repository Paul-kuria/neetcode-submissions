class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize
        maxA = 0
        l = 0
        r = len(heights)-1

        while l<r:
            # Calculate current area at ends (length * min_height)
            min_height = min(heights[l], heights[r])
            curr_area = (r-l) * min_height 

            # Check if maximum area
            maxA = max(maxA, curr_area)

            # Move pointers, till l<r
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxA

class Solution:
    def get_item(self, nums: List, target: int):
        l = 0
        r = len(nums) - 1 

        while l <= r:
            m = l + ( (r-l)//2 )
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1 
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Iterate through
        for row in matrix:
            ans = self.get_item(row, target)
            if ans:
                return True
        return False
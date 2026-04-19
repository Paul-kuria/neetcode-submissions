class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize placeholder list
        n = len(nums)
        output = [1] * n

        # iterate through list, calculating products of left side numbers
        for i in range(1, len(nums), 1):
            output[i] = output[i-1] * nums[i-1]
        
        # iterate through list, calculating products of right side & combining
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]
        
        return output
        
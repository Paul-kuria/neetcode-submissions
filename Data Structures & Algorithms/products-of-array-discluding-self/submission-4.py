class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step1: Prefix
        prefix = []
        prefix_running = 1 

        for i in range(len(nums)):
            # Add to prefix
            prefix.append(prefix_running)
            # Calculate running product
            prefix_running *= nums[i]
        

        # step2: Suffix
        suffix = []
        suffix_running = 1

        for i in range(len(nums)-1, -1, -1):
            # Add to suffix
            suffix.append(suffix_running)
            # Calculate running product
            suffix_running *= nums[i]

        # Reverse list
        suffix = suffix[::-1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        
        return ans
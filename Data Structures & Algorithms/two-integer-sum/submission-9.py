class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize output list
        ans = []

        # Iterate through list of integers using their indexes
        for i in range(len(nums)):
            # Find the larger number & smaller numbers that add up to target
            located_int = target - nums[i]
            # If match found for larger, store their indexes
            if located_int in nums :
                first = i
                second = nums.index(located_int)
        # Append the indexes outside the loop to prevent duplication
        ans.append(second)
        ans.append(first)
        
        return ans

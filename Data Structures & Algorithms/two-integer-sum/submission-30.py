class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps the number to its index
        seen = {}


        for i, num in enumerate(nums):
            complement = target - num

            # Check if the number we need is already in our dictionary
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
            
        

            


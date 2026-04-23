class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort our list in ascending
        nums.sort()

        res = []

        # Iterate over the list
        for i, val in enumerate(nums):
            # check that the second value is not equal to first 
            if i > 0 and val == nums[i-1]:
                continue
            
            # initialize our pointers, beginning and end
            l = i + 1 
            r = len(nums)-1
            
            # Squeeze on our list
            while l < r:
                threeSum = val + nums[l] + nums[r]
                # If summation is small, move left pointer up
                if threeSum < 0:
                    l += 1
                # If summation is big, move right pointer down
                elif threeSum > 0:
                    r -= 1
                # If it got the value
                else:
                    res.append( [val, nums[l], nums[r]] )
                    l += 1
                    # Ensure we dont recapture same value if next val is same as current
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res



       
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assuming every list has one pair of i and j.
        ans = []
        for i in range(len(nums)):
            located_int = target - nums[i]
            if located_int in nums :
                first = i
                second = nums.index(located_int)
        ans.append(second)
        ans.append(first)
        return ans

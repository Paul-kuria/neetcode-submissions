class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i, n in enumerate(nums):
            print(i, n)
            v2 = target - n 
            if v2 in ans:
                return[ans[v2], i]
            ans[n] = i

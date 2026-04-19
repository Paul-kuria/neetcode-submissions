class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store nums and their index
        ans = {} # val: index

        for idx, num in enumerate(nums):
            # Find the second number to be queried. Target - number in list
            v2 = target - num

            # If second number is also in the hashmap, return
            if v2 in ans:
                return [ans[v2], idx]
            ans[num] = idx

        
         

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = 1
            elif nums[i] in dct:
                dct[nums[i]] += 1

        for v in dct.values():
            if v > 1:
                return True
        return False
            #     print(v)
            #     return True
            # else:
            #     return False


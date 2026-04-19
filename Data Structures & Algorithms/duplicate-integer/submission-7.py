class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = set()
        for item in nums:
            if item not in new_list:
                new_list.add(item)
            else:
                return True
        return False

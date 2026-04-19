class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return true if any value appears more than once
        unique = set()
        for item in nums:
            if item in unique:
                return True
            unique.add(item)
        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for item in nums:
            if item in answer:
                return True
            else:
                answer.add(item)
        return False
        
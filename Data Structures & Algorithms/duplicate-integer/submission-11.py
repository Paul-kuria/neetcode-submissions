class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Input: array of nums
        Output: boolean
        TESTING: if any value is repeated, just that.
        '''
        result = set()

        for i in nums:
            if i in result:
                return True
            else:
                result.add(i)
        return False
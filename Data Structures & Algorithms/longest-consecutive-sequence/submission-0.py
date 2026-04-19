class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Check if list is populated or not
        if not nums:
            return 0
        
        # Step1: Create a set of nums for O(1) lookup
        num_set = set(nums)
        longest_streak = 0


        # Step2: Iterate through nums
        for num in num_set:
            # Check if its the start of a sequence
            if num -1 not in num_set: # (only consider starting points)
                current_num = num 
                current_streak = 1

                # Count the streak
                while current_num + 1 in num_set:
                    current_num += 1 
                    current_streak += 1 
                
                # Update longest streak
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
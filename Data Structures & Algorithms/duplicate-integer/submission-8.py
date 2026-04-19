class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a new set, as it contains non-duplicate, immutable objects
        new_list = set()

        # Iterate through the list of integers
        for item in nums:
            # If not present in the set, add it, if present, exit with a return True
            if item not in new_list:
                new_list.add(item)
            else:
                return True
        # If the program runs till here, means the list had no duplicates, return False
        return False

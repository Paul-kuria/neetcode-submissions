class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r: # move left & right pointers
            mid = (l + r) // 2
            
            # 1) If middle is target
            if target == nums[mid]:
                return mid
            
            # 2) Left portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # 3) Right portion
            if nums[r] >= nums[mid]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
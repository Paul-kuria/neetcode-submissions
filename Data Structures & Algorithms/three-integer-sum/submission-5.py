class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums = sorted(nums)

        ans = []
        for i in range(len(nums)-2):
            # Dont use the same fixed value twice
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Fix first value at position i, start left at i+1, start right at far end
            l = i + 1
            r = len(nums)-1

            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                if total_sum < 0:
                    l += 1 

                if total_sum > 0:
                    r -= 1

                if total_sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Duplicate handling.
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                
            
        return ans
                


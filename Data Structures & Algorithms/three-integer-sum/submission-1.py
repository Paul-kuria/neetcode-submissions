class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array in ascending order
        num_s = sorted(nums)

        # Initialize
        i = 0
        ans = [] 

        # Fix one value, and check for the compliments
        while i in range(len(num_s)-2):
            l = i+1
            r = len(num_s)-1

            while l<r:
                threeSum = num_s[l] + num_s[r] + num_s[i]

                if threeSum == 0:

                    ans.append([ num_s[l], num_s[r], num_s[i]] )
                    l += 1
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
            i += 1
        ans

        # Deduplicate
        result = []
        for i in ans:
            if i in result:
                continue
            result.append(i)
        return result


            

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            ans = numbers[i] + numbers[j]
            if ans < target:
                # Sum is too small, move i up
                i += 1
            elif ans > target:
                # Sum is too large, move j down
                j -= 1
            else:
                return [i+1, j+1]
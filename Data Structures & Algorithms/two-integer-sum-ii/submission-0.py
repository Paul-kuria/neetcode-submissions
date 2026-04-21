class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):
            second = target - val 
            print(f"Target: {target}, value_1: {val}, value_2: {second}")
            if second in numbers:
                return [i+1, numbers.index(second)+1]

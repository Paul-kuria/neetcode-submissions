class Solution:
    def multiply_numbers_array(self, arr: List):
        product = 1
        for item in arr:
            product *= item 
        return product 
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pointer_f = 0

        # Initialize variable to store the product
        current_product = 0
        res = []

        # Iterate thru array. For each element, check if its index is equal to i. If not, multiply the element by current_product
        for idx in range(0, len(nums)):
            if idx == pointer_f:
                numbers_before = nums[:idx]
                numbers_after = nums[idx+1:]
                current_product = self.multiply_numbers_array(numbers_before) * self.multiply_numbers_array(numbers_after)
                res.append(current_product)
                # print(numbers_before, numbers_after)
            pointer_f += 1
        
        return res
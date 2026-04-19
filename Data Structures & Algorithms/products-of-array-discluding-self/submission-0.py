class Solution:
    def multiply_values_in_list(self, mylist: List[int]) -> int:
        result = 1
        for x in mylist:
            result *= x 
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # Initialize empty output array
        res = [1] * length

        
 
        # Iterate through the indexes of the input array
        for i in range(length):
            print(f"iteration no: {i}")
            # When at the start of the list
            if i <= 0:
                mux = nums[i+1:length]
                value = self.multiply_values_in_list(mux)
                print(f"first: {mux}, value: {value}, index: {i}")
                res[i] = value

            # Anywhere within the list, look forwards and backwards 
            elif i >0 and i < length-1:
                before_current_index = nums[0:i] 
                after_current_index = nums[i+1:length]
                value1 = self.multiply_values_in_list(before_current_index)
                value2 = self.multiply_values_in_list(after_current_index)
                value = value1 * value2 
                print(f"middle value: {value},  index: {i}")
                res[i] = value

            # When at the end of the list
            elif i == length-1:
                mux = nums[0:length-1]
                value = self.multiply_values_in_list(mux)
                print(f"last: {mux}, value: {value},  index: {i}")
                res[i] = value

        return res
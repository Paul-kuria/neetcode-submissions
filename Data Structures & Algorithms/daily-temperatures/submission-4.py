class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                previous_temp, previous_index = stack.pop()
                result[previous_index] = index-previous_index
            
            stack.append([temperature, index])
        
        return result

       
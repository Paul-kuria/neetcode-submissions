class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Create final list, placeholder values with same length as temperatures
        RES = [0] * n 

        # Create waiting room stack
        stack = []

        # Iterate over list, checking if current value is greater than value at top of the stack
        for curr_idx, curr_item in enumerate(temperatures):
            while stack and curr_item > stack[-1][0]:
                # Check if larger, save to result
                popped_item, popped_idx = stack.pop()

                waiting_days = curr_idx - popped_idx 

                # Add to result
                RES[popped_idx] = waiting_days
            
            # Add value to stack
            stack.append([curr_item, curr_idx])
        
        return RES
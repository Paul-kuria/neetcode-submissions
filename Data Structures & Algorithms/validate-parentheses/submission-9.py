class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ')': '(',
            ']': '[' 
        }
        if len(s) == 0:
            return True 

        stack = []

        for char in s:
            # Add opening brackets
            if char not in mapping:
                stack.append(char)
            
            # Now for the closing brackets
            elif char in mapping:
                if stack:
                    last_bracket = stack.pop()
                    if last_bracket == mapping[char]:
                        continue
                    else:
                        return False
                else:
                    return False
        # Check if brackets were closed
        if len(stack) != 0:
            return False 

        return True
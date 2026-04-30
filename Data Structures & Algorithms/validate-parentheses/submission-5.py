class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ')': '(',
            ']': '[' 
        }

        # If item not even number, return false 
        length: int = len(s)


        if length % 2 < 0:
            return False 
        

        # Put items into a stack
        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                    
                latest = stack.pop()
                if latest != mapping[char]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
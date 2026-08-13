class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stackk = []

        # edge cases
        if len(s) < 2:
            return False 

        for i in s:
            if i not in dictionary:
                # Opening bracket
                stackk.append(i)

            elif len(stackk) < 1:
                # Closing bracket with nothing to match
                return False
            
            else:
                val = stackk.pop()
                opening_compliment = dictionary.get(i)
                
                if val != opening_compliment:
                    return False
                
                
        return len(stackk) == 0
            
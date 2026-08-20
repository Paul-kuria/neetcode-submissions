class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        operand = ["+", "-", "*", "/"]
        stack = []
        # Iterate over strings
        while i < len(tokens):
            if tokens[i] not in operand:
                val = int(tokens[i])
                stack.append(val)
                i += 1

            else:
                latter = stack.pop()
                former = stack.pop()

                if tokens[i] == "+":
                    v = former + latter 
                    i += 1

                elif tokens[i] == "-":
                    v = former - latter 
                    i += 1

                elif tokens[i] == "*":
                    v = former * latter 
                    i += 1

                elif tokens[i] == "/":
                    v = int(former / latter)
                    i += 1
                stack.append(v)        
        
        return stack.pop()


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
                if tokens[i] == "+":
                    latter = stack.pop()
                    former = stack.pop()
                    v = former + latter 
                    stack.append(v)
                    i += 1

                elif tokens[i] == "-":
                    latter = stack.pop()
                    former = stack.pop()
                    v = former - latter 
                    stack.append(v)
                    i += 1

                elif tokens[i] == "*":
                    latter = stack.pop()
                    former = stack.pop()
                    v = former * latter 
                    stack.append(v)
                    i += 1

                elif tokens[i] == "/":
                    latter = stack.pop()
                    former = stack.pop()
                    v = int(former / latter)
                    stack.append(v)
                    i += 1
        
        print(stack)
        return stack.pop()


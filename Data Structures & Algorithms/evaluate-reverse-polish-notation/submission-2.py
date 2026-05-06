from typing import List 
import operator 
import math 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        i = 0
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        while i < len(tokens):
            
            if tokens[i] not in ops:
                stack.append(tokens[i])
            elif tokens[i] in ops:
                print(tokens[i])
                v = int(stack.pop())
                v2 = int(stack.pop())
                stack.append(ops[tokens[i]](v2, v))
                
            print(stack)

            i += 1
          
        return int(stack[0])

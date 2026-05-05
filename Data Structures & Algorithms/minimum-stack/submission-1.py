class MinStack:
    def __init__(self):
        self.stack = [] 
    
    def push(self, val: int)->None:
        self.stack.append(val)
    
    def pop(self)->None:
        self.stack.pop()
    
    def top(self)->int:
        top = int(self.stack[-1])
        return top
    
    def getMin(self)->int:
        minimum = int(min(self.stack))
        return minimum
        

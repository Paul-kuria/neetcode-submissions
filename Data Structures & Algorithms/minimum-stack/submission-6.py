class MinStack:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, val: int) -> None:
        # Add to stack
        self.stack.append(val)

        # If temp array is not empty, save min value at the end
        if self.temp:
            min_val = min(self.temp[-1], val)
            self.temp.append(min_val)
        else:
            self.temp.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.temp.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        # Check for most min element
        return self.temp[-1]

        

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum = val
            return 
        
        self.stack.append(val - self.minimum)
        self.minimum = min(self.minimum, val)       

    def pop(self) -> None:
        top = self.stack.pop()
        
        if top < 0:
            ret = self.minimum
            mini = ret - top
            self.minimum = mini
            return ret
        else:
            ret = top + self.minimum
            return ret

        

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            ret = self.minimum
            return ret
        else:
            ret = top + self.minimum
            return ret

        

    def getMin(self) -> int:
        return self.minimum
        

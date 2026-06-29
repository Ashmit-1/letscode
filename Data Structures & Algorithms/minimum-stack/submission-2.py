class MinStack:
    def binSearch(self, arr, val):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if arr[mid] > val:
                    end = mid - 1
                elif arr[mid] < val:
                    start = mid + 1
                else:
                    return mid
            return start

    def __init__(self):
        self.stack = []
        self.min_stack = []
       
        

    def push(self, val: int) -> None:
        
        
        
        self.stack.append(val)
        if not self.min_stack or val > self.min_stack[-1]: 
            self.min_stack.append(val)
            return 
        index = self.binSearch(self.min_stack, val)
        self.min_stack.insert(index, val)
        
        

    def pop(self) -> None:
        
        ele = self.stack.pop()

        index = self.binSearch(self.min_stack, ele)
        self.min_stack.pop(index)
      
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.min_stack[0]
        

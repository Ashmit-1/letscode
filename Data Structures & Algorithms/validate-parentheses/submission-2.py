class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        for i in s:
            if i not in close: stack.append(i)
            else:
                if len(stack) == 0: return False
                if stack.pop() != close[i]: return False
        if stack:
            return False
        return True
        
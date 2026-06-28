class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        for i in s:
            if i in open: stack.append(i)
            else:
                if len(stack) == 0: return False
                if stack.pop() != close[i]: return False
        if stack:
            return False
        return True
        
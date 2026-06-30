class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][1] > temp:
                stack.append([i, temp])
                result.append(0)
            else:
                while stack and stack[-1][1] < temp:
                    ind, t = stack.pop()
                    result[ind] = i - ind
                stack.append([i, temp])
                result.append(0)
        return result
        
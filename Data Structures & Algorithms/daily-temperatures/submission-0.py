class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1] > temp:
                stack.append(temp)
                result.append(0)
            else:
                left = i
                count = 0
                while left > 0:
                    count+=1
                    if result[left-1] == 0 and temp > stack[left-1]:
                        result[left-1] = count
                    left-=1
                result.append(0)
                stack.append(temp)
        return result
            


        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = []

        for i, hgt in enumerate(heights):
            if not stack:
                stack.append(i)
                left.append(-1)
            elif heights[stack[-1]] < hgt:
                left.append(stack[-1])
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= hgt:
                    stack.pop()

                if stack:
                    left.append(stack[-1])
                else:
                    left.append(-1)
                stack.append(i)
        stack = []
        right = []

        for i in range(n-1, -1, -1):
            if not stack:
                right.append(n)
                stack.append(i)
            elif heights[stack[-1]] < heights[i]:
                right.append(stack[-1])
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    right.append(n)
                else:
                    right.append(stack[-1])
                stack.append(i)
        
        res = 0
        for i in range(n):
            print(heights[i], right[n-1-i], left[i])
            res = max(res, (right[n-i-1] - left[i] - 1)*heights[i])
        return res



        

            
        





        
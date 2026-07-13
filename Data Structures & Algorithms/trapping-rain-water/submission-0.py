class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxLeft, maxRight = [], []
        runLeft, runRight = -1, -1
    
        while left < len(height):
            maxLeft.append(runLeft)
            maxRight.append(runRight)
            
            runLeft = max(runLeft, height[left])
            runRight = max(runRight, height[right])

            left+=1
            right-=1

        water = []
        for i, h in enumerate(height):
            water.append(min(maxLeft[i], maxRight[len(height) - 1 - i]) - h)
            # print(maxLeft[i], maxRight[len(height) - i - 1], h, water[-1])
        maxWater = 0
        for i, w in enumerate(water):
            if w > 0:
                maxWater+=w
        return maxWater
        
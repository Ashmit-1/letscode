class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        min_k = piles[-1]

        n = len(piles)
        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            t = 0
            for p in piles:
                if p <= mid:
                    t+=1
                else:
                    t+=math.ceil(p / mid)
            if t > h:
                left = mid + 1
            else:
                min_k = min(min_k, mid)
                right = mid - 1
        return min_k
            

        
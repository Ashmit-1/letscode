class Solution:
    def countBits(self, n: int) -> List[int]:
        from functools import lru_cache

        @lru_cache
        def countBits(n, count=0):
            if n == 0: return count
            if n & 1:
                return countBits(n>>1, count+1)
            else:
                return countBits(n>>1, count)
        
        ret = []
        for i in range(n+1):
            res = 0
            res+=countBits(i)
            ret.append(res)
        return ret
        
        
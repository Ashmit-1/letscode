class Solution:
    def countBits(self, n: int) -> List[int]:
        from functools import lru_cache

        @lru_cache
        def countBits(n):
            count = 0
            while n != 0:
                if n & 1: count+=1
                n = n >> 1
            return count
        
        ret = []
        for i in range(n+1):
            res = 0
            res+=countBits(i)
            ret.append(res)
        return ret
        
        
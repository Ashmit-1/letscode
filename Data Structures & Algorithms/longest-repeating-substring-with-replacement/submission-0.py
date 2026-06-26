class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        res, maxFreq = 0, 0
        for i in range(0, len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            maxFreq = max(maxFreq, seen[s[i]])
            while i - left + 1 - maxFreq > k:
                seen[s[left]]-=1
                left+=1
            res = max(res, i - left + 1)
        return res

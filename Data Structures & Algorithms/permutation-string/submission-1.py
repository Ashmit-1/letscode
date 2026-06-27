class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter
        hm = Counter(s2[:len(s1)])
        hms1 = Counter(s1)
        left = 0
        if hm == hms1: return True
        for i in range(len(s1),len(s2)):
            hm[s2[left]]-=1
            if hm[s2[left]] == 0: del hm[s2[left]]
            hm[s2[i]]  = hm.get(s2[i], 0) + 1
            left+=1
            if hm == hms1: return True
        return False

        
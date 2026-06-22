class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            s_s = "".join(sorted(s))
            if s_s in seen:
                seen[s_s].append(s)
            else:
                seen[s_s] = [s]
        return list(seen.values())

        
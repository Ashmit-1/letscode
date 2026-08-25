class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for st in strs:
            key = "".join(sorted([s for s in st]))
            if key in hashMap:
                hashMap[key].append(st)
            else:
                hashMap[key] = [st]
        return list(hashMap.values())
        
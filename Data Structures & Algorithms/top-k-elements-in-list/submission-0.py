class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ctr = Counter(nums)
        lst = []
        for num in ctr:
            lst.append([num, ctr[num]])
        return [ele[0] for ele in sorted(lst, key=lambda x : x[1], reverse=True)[:k]]

        
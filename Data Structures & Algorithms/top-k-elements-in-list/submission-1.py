class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ctr = Counter(nums)
        bucket = [0] * (len(nums)+1)
        for ele, freq in ctr.items():
            if bucket[freq] != 0:
                bucket[freq].append(ele)
            else:
                bucket[freq] = [ele]
        res = []
        for i in bucket[::-1]:
            if i != 0:
                res.extend(i)
            if len(res) > k:
                break
        return res[:k]

        
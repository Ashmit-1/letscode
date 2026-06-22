class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for num in nums:
            if num == 0:
                count+=1
                if count == 2:
                    return [0] * len(nums)
            else:
                prod*=num
        res = []
        if count == 1:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(prod // num)
        return res

        
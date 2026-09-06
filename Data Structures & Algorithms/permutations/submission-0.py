class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(ind, nums, ans):
            if ind == len(nums):
                ans.append(nums.copy())
                return 
            for i in range(ind, len(nums)):
                nums[ind], nums[i] = nums[i], nums[ind]
                helper(ind+1, nums, ans)
                nums[ind], nums[i] = nums[i], nums[ind]
        ans = []
        helper(0, nums, ans)
        return ans


        
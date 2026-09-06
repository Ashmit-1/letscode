class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(ind, target, nums, ls, ans):
        
            if ind == len(nums):
                if target == 0:
                    ans.append(ls.copy())
                return
            if nums[ind] <= target:
                ls.append(nums[ind])
                helper(ind, target-nums[ind], nums, ls, ans)
                ls.pop()
            helper(ind+1, target, nums, ls, ans)
        ans = []
        helper(0, target, nums, [], ans)
        return ans
            
            
        
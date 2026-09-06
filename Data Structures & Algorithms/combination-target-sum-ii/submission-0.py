class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(ind, target, nums, ls, ans):
           
            if target == 0:
                ans.append(ls.copy())
                return 
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i-1]: continue
                if nums[i] <= target:
                    ls.append(nums[i])
                    helper(i+1, target-nums[i], nums, ls, ans)
                    ls.pop()
                else:
                    break
                
                
        ans = []
        helper(0, target, sorted(candidates), [], ans)
        return ans        
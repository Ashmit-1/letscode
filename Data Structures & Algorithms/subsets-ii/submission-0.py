class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(ind, nums, ls, ans):

            ans.append(ls.copy())

            for i in range(ind, len(nums)):
                if ind != i and nums[i] == nums[i-1]:
                    continue
                ls.append(nums[i])
                helper(i+1, nums, ls, ans)
                ls.pop()
        ans = []
        helper(0, sorted(nums), [], ans)
        return ans
        
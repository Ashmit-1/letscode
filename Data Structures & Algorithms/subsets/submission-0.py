class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find_sub(ind, nums, ls, ans):
            if ind == len(nums):
                ans.append(ls[:])
                return 
            ls.append(nums[ind])
            find_sub(ind+1, nums, ls, ans)
            ls.pop()
            find_sub(ind+1, nums, ls, ans)
        ans = []
        find_sub(0, nums, [], ans)
        return ans
        
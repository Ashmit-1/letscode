class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            "2":['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z'],
            "0" : [" "]
        }
        def helper(ind, d, ls, ans):
            if len(d) == 0: return
            if ind == len(d):
                ans.append("".join(ls))
                return 
            for i in hm[d[ind]]:
                ls.append(i)
                helper(ind+1, d, ls, ans)
                ls.pop()
        ans = []
        helper(0, digits, [], ans)
        return ans
            
        
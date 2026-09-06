class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(ind, op, cl, ls, ans):
            if ind == n*2:
                ans.append("".join(ls.copy()))
                return 
            if op == 0 or op == cl:
                ls.append("(")
                helper(ind+1, op+1, cl, ls, ans)
                ls.pop()
            elif op < n and cl < n and op > cl:
                ls.append("(")
                helper(ind+1, op+1, cl, ls, ans)
                ls.pop()

                ls.append(")")
                helper(ind+1, op, cl+1, ls, ans)
                ls.pop()
            elif op == n:
                ls.append(")")
                helper(ind+1, op, cl+1, ls, ans)
                ls.pop()
        ans = []
        helper(0, 0, 0, [], ans)
        return ans


        
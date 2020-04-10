class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def helper(temp='',left=0,right=0):
            if len(temp)==n*2:
                res.append(temp)
                return
            if left<n:
                helper(temp+'(',left+1,right)
            if right<left:
                helper(temp+')',left,right+1)

        helper()
        return res

res=Solution()
print(res.generateParenthesis(3))
            
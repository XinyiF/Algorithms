class Solution(object):
    def reverse(self, x):
        flag=False
        if x<0:
            flag=True
        x=str(x)
        if flag:
            x=x[1:]
        res=x[::-1]
        if flag:
            res=-int(res)
        else:
            res=int(res)
        if -2 ** 31 < res < 2 ** 31 - 1:
            return res
        return 0


res=Solution()
print(res.reverse(-230))
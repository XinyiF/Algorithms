class Solution:
    def replaceSpace(self, s):
        res=''
        for i in range(len(s)):
            if s[i]==' ':
                res+='%20'
            else:res+=s[i]
        return res

s='we are happy'
res=Solution()
resu=res.replaceSpace(s)
print(resu)

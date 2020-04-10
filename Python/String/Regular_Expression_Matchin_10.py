#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.

class Solution(object):
    def isMatch(self, s,p):
        count={}
        count[(0,0)]=True
        for i in range(len(p)):
            if p[i]=='*':
                count[(i+1,0)]=count[(i-1,0)]
            else:count[(i+1,0)]=False
        for i in range(len(s)):
            count[(0,i+1)]=False
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i]==p[j] or p[j]=='.': count[(j+1,i+1)]=count[(j,i)]
                elif p[j]=='*':
                    if p[j-1]==s[i] or p[j-1]=='.':
                        count[(j + 1, i + 1)]=count[(j-1,i+1)] or count[(j+1,i)]
                    else:
                        count[(j+1,i+1)]=count[(j-1,i+1)]
                else: count[(j+1,i+1)]=False
        return count[(len(p),len(s))]


s="mis"
p="mis*"

res=Solution()
print(res.isMatch(s,p))




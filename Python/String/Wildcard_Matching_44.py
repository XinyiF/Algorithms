#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).
class Solution(object):
    def isMatch(self, s, p):
        count={}
        count[(0,0)]=True
        for i in range(len(s)):
            count[(0,i+1)]=False
        i,index=0,0
        while i < len(p):
            if i==0 and p[i]=='*':
                while i< len(p) and p[i]=='*':
                    count[(i + 1, 0)] = True
                    for j in range(len(s)):
                        count[(i+1,j+1)]=True
                        index=i+1
                    i+=1
            count[(i + 1, 0)] = False
            i+=1

        if index==len(p): return count[(len(p),len(s))]
        for i in range(len(s)):
            for j in range(index,len(p)):
                if p[j]==s[i] or p[j]=='?':
                    count[(j+1,i+1)]=count[(j,i)]
                elif p[j]=='*':
                    count[(j + 1, i + 1)] = count[(j, i + 1)] or count[(j, i)] or count[(j+1,i)]
                else:
                    count[(j+1, i+1)] =False
        return count[(len(p),len(s))]


s="aaaa"
p='***a'
res=Solution()
print(res.isMatch(s,p))

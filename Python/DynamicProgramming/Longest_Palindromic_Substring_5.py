#Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)<2 or len(s)==2 and s[0]==s[1]:return s
        if len(s)==2 and s[0]!=s[1]:return s[0]
        count={}
        for i in range(len(s)-1):
            flag=0
            left,right=i-1,i+1
            cur=s[i]
            Left, Right=-1,-1
            cur1=''
            if s[i]==s[i+1]:
                flag=1
                Left,Right=i-1,i+2
                cur1=s[i]+s[i+1]
            # s[i] is the center
            while left>=0 and right<len(s):
                if s[left]==s[right]:
                    cur=s[left]+cur+s[right]
                    left-=1
                    right+=1
                else:
                    break
            left += 1
            right -= 1
            count[cur]=right-left+1
            # s[i]+s[i+1] is the center
            while flag==1 and Left>=0 and Right<len(s):
                if s[Left]==s[Right]:
                    cur1=s[Left]+cur1+s[Right]
                    Left-=1
                    Right+=1
                else:
                    break
            Left += 1
            Right -= 1
            count[cur1]=Right-Left+1
        return max(count,key=count.get)

    def CenterExpand(self,left,right,cur,count,s):
        while left>=0 and right<len(s):
            if s[left]==s[right]:
                cur = s[left] + cur + s[right]
                left-=1;right+=1
            else:break
        left+=1;right-=1
        count[cur]=right-left+1

    def longestPalindrome_new(self, s):
        if len(s)<2 or len(s)==2 and s[0]==s[1]:return s
        if len(s)==2 and s[0]!=s[1]:return s[0]
        count={}
        for i in range(len(s)-1):
            cur1,cur2=s[i],''
            self.CenterExpand(i-1,i+1,cur1,count,s)
            self.CenterExpand(i,i+1,cur2,count,s)
        return max(count,key=count.get)





str="aaaabbccbb"
res=Solution()
s=res.longestPalindrome_new(str)
print(s)






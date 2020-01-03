#Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.

class Solution(object):
    def CenterExpand_neib(self, left, right, count, cur, s):
        flag=0
        while left>=0 and right<len(s):
            if s[left]==s[right]:flag=1;left-=1;right+=1
            else:break
        if left==-1 or flag==0 and left==0:
            cur=s
            for i in range(right,len(s)):
                cur=s[i]+cur
            count[cur] = len(cur)


    def CenterExpand_betw(self, left, right, count, cur, s):
        while left>=0 and right<len(s):
            if s[left]==s[right]:left-=1;right+=1
            else:break
        if left==-1:
            cur=s
            for i in range(right, len(s)):
                cur = s[i] + cur
            count[cur] = len(cur)

    def shortestPalindrome1(self, s):
        count={}
        cur=''
        rev=s[::-1]
        flag=0
        if len(s)<=1:return s
        index = 0
        for i in range(int(len(s)/2)):
            cur=cur+s[i]
            if cur==rev[len(s)-(i+1)-(i+1):len(s)-(i+1)]:
                flag=0
                count[i]=index
                index+=1
            if cur==rev[len(s)-(i+1)-(i+1)-1:len(s)-(i+1)-1]:
                flag=1
                count[i] = index
                index += 1
        if not count:end=1
        else:
            mid=max(count,key=count.get)
            if flag==0:end=(mid+1)*2
            if flag==1:end=(mid+1)*2+1
        cur=s
        for i in range(end,len(s)):
            cur=s[i]+cur
        return cur

    def shortestPalindrome2(self, s):
        length = len(s)
        count=[]
        if length <= 1: return s
        for i in range(1,int(length/2)+1):
            cur,sub1,sub2=s[0:i],s[i:2*i],s[i+1:2*i+1]
            if cur== sub1[::-1] or cur==sub2[::-1]:count.append(i)
        if not count: return s[1:length][::-1]+s
        if count[len(count)-1]==int(length/2) and s[0:i]==s[i+1:length]:return s
        else:i=count[len(count)-1]
        cur=s[0:i]
        if cur==s[i:2*i][::-1]:return s[2*i:length][::-1]+s
        elif cur==s[i+1:i*2+1][::-1]:return s[2*i+1:length][::-1]+s






str="aaaaa" #hgfe dcba
res=Solution()
s=res.shortestPalindrome2(str)
print(s)
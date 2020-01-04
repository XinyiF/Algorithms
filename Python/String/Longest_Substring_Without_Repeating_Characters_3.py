#Given a string, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:return 0
        if len(s) == 1: return 1
        count={}
        left,right=0,1
        while right<len(s):
            if right==len(s)-1 and not s[right] in s[left:right]:
                count[s[left:]] = len(s[left:])
            if not s[right] in s[left:right]:
                right+=1
            else:
                count[s[left:right]]=len(s[left:right])
                left += s[left:right].index(s[right])+1
                right+=1
        if left==0 and right==len(s):
            return len(s)
        return max(count.values())



s="aab"
res=Solution()
#print(res.lengthOfLongestSubstring(s))
count=res.lengthOfLongestSubstring(s)
print(count)



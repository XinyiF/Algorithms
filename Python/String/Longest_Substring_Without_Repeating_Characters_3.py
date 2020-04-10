#Given a string, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:return 0
        if len(s) == 1: return 1
        count={}
        left,right=0,1
        while right<len(s):
            if not s[right] in s[left:right]:
                count[s[left:right+1]]=len(s[left:right+1])
                right+=1
            else:
                left+=1
        return max(count.values())



s="abcdacdfg"
res=Solution()
#print(res.lengthOfLongestSubstring(s))
count=res.lengthOfLongestSubstring(s)
print(count)



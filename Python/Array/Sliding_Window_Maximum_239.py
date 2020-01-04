#Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums)==0:return
        left,right,res=0,k-1,[]
        while right<len(nums):
            res.append(max(nums[left:right+1]))
            left+=1
            right+=1
        return res



nums = [1,3,-1,-3,5,3,6,7]
k = 3
res=Solution()
resu=res.maxSlidingWindow(nums,k)
print(resu)
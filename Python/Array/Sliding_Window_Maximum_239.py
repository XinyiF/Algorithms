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

    def maxSlidingWindow_dq(self, nums, k):
        if len(nums) == 0: return
        if k==1:return nums
        left, right, res = 0, k-1, []
        Max=max(nums[0:k])
        index=nums[0:k].index(Max)
        while right < len(nums):
            if index >=left:
                Max=max(Max,nums[right])
            else:
                Max=max(nums[left:right+1])
            index = nums[left:right + 1].index(Max)
            res.append(Max)
            left += 1
            right += 1
        return res







nums = [7,2,4]
k = 2
res=Solution()
resu=res.maxSlidingWindow_dq(nums,k)
print(resu)

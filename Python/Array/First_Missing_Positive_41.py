#Given an unsorted integer array, find the smallest missing positive integer.
class Solution(object):
    def firstMissingPositive(self, nums):
        flag = 0;length = len(nums)
        if(length==0 or length==1 and nums[0]<=0 or length==1 and nums[0]>1):return 1
        for i in range(length):
            if (nums[i] == 1):
                flag = 1
            elif(nums[i]<=0):
                nums[i]=1
        if (flag == 0):
            return 1
        nums = sorted(nums)
        j=2
        while(True):
            if(j not in nums):
                return j
            else:
                j+=1


nums = [3,4,-1,1]
length = Solution()
a = length.firstMissingPositive(nums)
print(a)

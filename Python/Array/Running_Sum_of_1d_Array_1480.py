class Solution(object):
    def runningSum(self, nums):
        res=[]
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res
num=[1,2,3,4]
res=Solution()
print(res.runningSum(num))
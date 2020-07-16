class Solution(object):
    def numIdenticalPairs(self, nums):
        res=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    res+=1
        return res

num = [1,2,3,1,1,3]
res = Solution()
print(res.numIdenticalPairs(num))



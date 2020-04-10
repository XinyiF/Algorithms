#Find all unique triplets in the array which gives the sum of zero
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        if len(nums) < 3 or nums[0]>0: return []
        res,record,i=[],{},0
        while i < len(nums)-2:
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1] :
                        left += 1
                    while  left<right and nums[right]==nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
            while i < len(nums)-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


s=[0,0,0]
res=Solution()
print(res.threeSum(s))





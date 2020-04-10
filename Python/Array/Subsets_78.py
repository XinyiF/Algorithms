#Given a set of distinct integers, nums, return all possible subsets (the power set).

class Solution(object):
    def subsets(self, nums):
        count,res={},[]
        count[0]=[]
        res.append(count[0])
        if not nums: return res
        length=len(nums)
        index=1
        for i in range(length):
            for j in range(index):
                sub=count[j]+[nums[i]]
                if not sub in count.values():
                    count[index]=sub
                    res.append(sub)
                    index+=1
        return res


nums=[1,2,3]
res=Solution()
print(res.subsets(nums))


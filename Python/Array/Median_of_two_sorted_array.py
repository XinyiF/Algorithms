class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num=nums1+nums2
        num=sorted(num)
        if len(num)%2==0:
            return (num[len(num)//2]+num[len(num)//2-1])/2
        else:
            return num[len(num)//2]

n1=[1,3]
n2=[2]
res=Solution()
print(res.findMedianSortedArrays(n1,n2))
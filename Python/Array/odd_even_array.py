#put odd value to the first half of an array and even to the second part
class Solution:
    def reOrderArray(self, array):
        return list(filter(lambda x:x%2,array))+list(filter(lambda x:x%2==0,array))


a=[1,2,3,4,5,6]
res=Solution()
print(res.reOrderArray(a))
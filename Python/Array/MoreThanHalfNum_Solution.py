#find the number whose is majority in the array
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:return 0
        half=len(numbers)//2+1
        count={}
        for i in numbers:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]==half:
                return i
        return 0
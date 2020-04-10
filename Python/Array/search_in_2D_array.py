class Solution:
    def Find(self, target, array):
        high,length=len(array),len(array[0])
        i,j=high-1,0
        while i>=1 and j<=length-2:
            if array[i][j]<target:j+=1
            else:i-=1
            if array[i][j]==target:
                return True
        return False


array=[[1,2,3],[4,5,6]]
res=Solution()
print(res.Find(7,array))

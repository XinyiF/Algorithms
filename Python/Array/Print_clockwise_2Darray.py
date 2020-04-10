#print a 2D array clockwise
class Solution:
    def printMatrix(self, matrix):
        if not matrix:return
        row,col=len(matrix),len(matrix[0])
        res,count=[],{}
        i,j=0,0
        while not (i,j) in count:
            while j<col and not (i,j) in count:
                res.append(matrix[i][j])
                count[i,j]=matrix[i][j]
                j += 1
            j-=1
            i+=1
            while i<row and not (i,j) in count:
                res.append(matrix[i][j])
                count[i, j] = matrix[i][j]
                i += 1
            i-=1
            j-=1
            while j>=0 and  not (i,j) in count:
                res.append(matrix[i][j])
                count[i,j] = matrix[i][j]
                j-=1
            j+=1
            i-=1
            while i>=0 and not (i,j) in count:
                res.append(matrix[i][j])
                count[i, j] = matrix[i][j]
                i-=1
            i+=1
            j+=1
        return res

    def print(self,matrix):
        res,count=[],{}
        for i in range(-1,len(matrix[0])+1):
            count[-1,i]=1
        for i in range(-1,len(matrix)+1):
            count[i,len(matrix[0])]=1
        for i in range(len(matrix[0]),-2,-1):
            count[len(matrix),i]=1
        for i in range(len(matrix),-2,-1):
            count[i,-1]=1
        i,j=0,0
        while not (i, j) in count:
            while not (i, j) in count:
                res.append(matrix[i][j])
                count[i, j] = 1
                j += 1
            j -= 1
            i += 1
            while not (i, j) in count:
                res.append(matrix[i][j])
                count[i, j] = 1
                i += 1
            i -= 1
            j -= 1
            while not (i, j) in count:
                res.append(matrix[i][j])
                count[i, j] = 1
                j -= 1
            j += 1
            i -= 1
            while not (i, j) in count:
                res.append(matrix[i][j])
                count[i, j] = 1
                i -= 1
            i += 1
            j += 1
        return res




a=[[1,2,3,4],[5,6,7,8]]
res=Solution()
print(res.print(a))

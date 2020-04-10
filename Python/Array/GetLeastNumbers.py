#Find the k smallest values in array
class Solution:
    def GetLeastNumbers_Solution_usefunc(self, tinput, k):
        if k>len(tinput) or not tinput:
            return []
        tinput=sorted(tinput)
        res=[]
        for i in range(k):
            res.append(tinput[i])
        return res



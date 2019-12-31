#Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
# there are such that A[i] + B[j] + C[k] + D[l] is zero.
#To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count ={}
        for a in A:
            for b in B:
                if(a+b) in count:
                    count[a+b]+=1
                else:
                    count[a+b]=1
        counter=0
        for c in C:
            for d in D:
                if(-c-d in count):
                    counter+=count[-c-d]
        return counter

A=[1,2]
B=[-2,-1]
C=[-1,2]
D=[0,2]
res=Solution()
res.fourSumCount(A,B,C,D)
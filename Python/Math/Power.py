#power function...
class Solution:
    def Power(self, base, exponent):
        if exponent==0:return 1
        counter=1
        multi=1
        while counter<=abs(exponent):
            multi*=base
            counter+=1
        if exponent>0:
            return multi
        else:
            return 1./multi

res=Solution()
print(res.Power(2,-3))


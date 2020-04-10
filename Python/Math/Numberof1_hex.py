#Enter an integer and output the number of 1s in the binary representation of the number.
# Negative numbers are represented by two's complement.
class Solution:
    def NumberOf1(self, n):
        if n==0 or n==1:return n
        num=n
        n=abs(n)
        tf,counter,res = [],0,[]
        for i in range(32):
            res.append(0)
        while n != 0:
            tf.append(n - (n // 2) * 2)
            if n - (n // 2) * 2==1:
                counter+=1
            n = n // 2
        if num>0 or num==-2147483648:
            return counter
        else:
            res=res[:len(res)-len(tf)]+tf[::-1]
            for i in range(len(res)):
                if res[i]==1:res[i]=0
                else:res[i]=1
            if res[len(res)-1]==0:
                res[len(res)-1]=1
                return res.count(1)
            else:
                for i in range(len(res)-1,-1,-1):
                    if res[i]==0:
                        res[i]=1
                        break
                    else:
                        res[i]=0
                return res.count(1)



res=Solution()
print(res.NumberOf1(-1))
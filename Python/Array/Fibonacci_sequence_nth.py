#return the nth term of a fibonacci sequence
class Solution:
    def Fibonacci(self, n):
        f,i=[0,1,1],3
        if n<3:return f[n]
        while i<=n:
            f.append(f[i-1]+f[i-2])
            i+=1
        return f[len(f)-1]

res=Solution()
print(res.Fibonacci(4))


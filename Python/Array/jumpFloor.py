class Solution:
    def jumpFloor(self, number):
        f, i = [0,1,2],3
        if number < 3: return f[number]
        while i <= number:
            f.append(f[i - 1] + f[i - 2])
            i += 1
        return f[len(f) - 1]



# 1  2   3     4
# 1  2  2+1   3+2


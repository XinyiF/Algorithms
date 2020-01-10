#frog can jump 1 or 2 level at one time, how many possibilities for him to jump up to level n floor
class Solution:
    def jumpFloor(self, number):
        f, i = [0,1,2],3
        if number < 3: return f[number]
        while i <= number:
            f.append(f[i - 1] + f[i - 2])
            i += 1
        return f[len(f) - 1]

#frog can jump 1~n level at one time, how many possibilities for him to jump up to level n floor
    def jumpFloorII(self, number):
        f, i = [0, 1, 2], 3
        if number < 3: return f[number]
        while i <= number:
            f.append(f[i - 1]*2)
            i += 1
        return f[len(f) - 1]




# 1  2   3      4
# 1  2   4   4+2+1+1


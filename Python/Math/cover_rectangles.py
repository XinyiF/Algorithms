#We can use 2 * 1 small rectangles to cover larger rectangles horizontally or vertically.
# How many ways are there to cover a 2 * n large rectangle with n 2 * 1 small rectangles without overlapping?
class Solution:
    def rectCover(self, number):
        f,i=[0,1,2],3
        if number < 3: return f[number]
        while i<=number:
            f.append(f[i-2]+f[i-1])
            i+=1
        return f[len(f)-1]


#1   2     3     4
#1   2    2+1   3+2
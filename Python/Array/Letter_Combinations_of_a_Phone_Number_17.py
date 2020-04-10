# Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def helper(cur,next_digi):
            if not next_digi:
                res.append(cur)
            else:
                for i in phone[next_digi[0]]:
                    helper(cur+i, next_digi[1:])
        res = []
        if digits:
            helper('', digits)
        return res


dig='23'
res=Solution()
print(res.letterCombinations(dig))

a=[1,2,3]
c,d,e=map(int,a)
print(c,d,e)



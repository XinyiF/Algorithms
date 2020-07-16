class Solution(object):
    def letterCombinations(self, digits):
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def helper(temp,next_digit):
            if len(next_digit)==0:
                res.append(temp)
            else:
                for letter in KEY[next_digit[0]]:
                    helper(temp+letter,next_digit[1:])

        res=[]
        temp=""
        if digits:
            helper(temp,digits)
        return res




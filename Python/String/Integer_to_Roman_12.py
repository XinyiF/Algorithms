#https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num: int) -> str:
        ones_place=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens_place=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds_place=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands_place=["", "M", "MM", "MMM"]
        return thousands_place[num//1000]+hundreds_place[num%1000//100]+tens_place[num%100//10]+ones_place[num%10]



res=Solution()
print(res.intToRoman(1994))
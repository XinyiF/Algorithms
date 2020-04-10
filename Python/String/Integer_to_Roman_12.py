class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        ones_place=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens_place=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds_place=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands_place=["", "M", "MM", "MMM"]
        return thousands_place[num//1000]+hundreds_place[num%1000//100]+tens_place[num%100//10]+ones_place[num%10]



res=Solution()
print(res.intToRoman(1994))
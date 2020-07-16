class Solution(object):
    def shuffle(self, nums, n):
        res=[]
        num1=nums[:n]
        num2=nums[n:2*n]
        for i in range(n):
            res.append(num1[i])
            res.append(num2[i])
        return res

    def kidsWithCandies(self, candies, extraCandies):
        m=max(candies)
        res=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                res.append(1)
            else:
                res.append(0)
        return res

    def defangIPaddr(self, address):
        res=""
        for i in range(len(address)):
            if address[i]==".":
                res+="[.]"
            else:
                res+=address[i]
        return res

    def numberOfSteps(self, num):
        step=0
        while num!=0:
            if num%2==0:
                num=num//2
                step+=1
            else:
                num-=1
                step += 1
        return step

    def numJewelsInStones(self, J, S):
        res=0
        for i in S:
            if i in J:
                res+=1
        return res

    def groupThePeople(self, groupSizes):
        dic,res={},[]
        for i in range(len(groupSizes)):
            if groupSizes[i] in dic:
                dic[groupSizes[i]].append(i)
            else:
                dic[groupSizes[i]]=[i]
            if len(dic[groupSizes[i]])==groupSizes[i]:
                res.append(dic[groupSizes[i]])
                del dic[groupSizes[i]]
        return res

    def convert(self, s, numRows):
        if len(s)<=numRows:
            return s
        iter=[]
        for i in range(1,numRows+1):
            iter.append(i)
        for j in range(numRows-1,1,-1):
            iter.append(j)
        dic,res,step={},"",0
        while step<len(s):
            for i in iter:
                if step>=len(s):
                    break
                if not i in dic:
                    dic[i]=s[step]
                else:
                    dic[i]+=s[step]
                step+=1

        for i in range(1,numRows+1):
            res+=dic[i]
        return res

    def myAtoi(self, str):
        str = str.strip()

        if "+-" in str or "++" in str or "--" in str:
            return 0

        str = str.strip("+")
        if not str: return 0

        ref = "0123456789"

        IsNeg = False
        if str[0] == "-":
            IsNeg = True
            str = str[1:]
            if len(str) == 0:
                return 0
        temp = ""
        for i in range(len(str)):
            if not str[i] in ref:
                break
            else:
                temp += str[i]
        iter, res = 0, 0
        for i in range(len(temp) - 1, -1, -1):
            res += int(temp[i]) * pow(10, iter)
            iter += 1

        if res >= pow(2, 31):
            if not IsNeg:
                return pow(2, 31) - 1
            else:
                return -pow(2, 31)

        if IsNeg:
            res = -res
        return res




res = Solution()
s="42"
print(res.myAtoi(s))


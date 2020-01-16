#Give an array and return the sum of its largest consecutive subsequence
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:return
        sum,Max=0,[]
        for i in range(len(array)):
            if sum<0:
                sum = array[i]
            else:
                sum+=array[i]
            Max.append(sum)
        res=max(Max)
        return res


s=[8,-8,5]
res=Solution()
print(res.FindGreatestSumOfSubArray(s))
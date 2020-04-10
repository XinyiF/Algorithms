#longest subarray that the difference of each pair is less than 1
def pickingNumbers(a):
    # Write your code here
    Max= 0
    a=sorted(a)
    for i in range(len(a)):
        temp=[]
        temp.append(a[i])
        for j in range(i+1,len(a)):
            if abs(a[j]-a[i])<=1:
                temp.append(a[j])
                Max=max(Max,len(temp))
            else:
                Max=max(Max,len(temp))
                break
    return Max


s=[3,3,3,3,3]
print(pickingNumbers(s))
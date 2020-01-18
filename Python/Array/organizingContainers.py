#https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
def organizingContainers(container):
    for i in range(len(container)):
        flag=0
        for j in range(len(container[0])):
            Sum_ref=sum(container[i])-container[i][j]
            Sum_comp=0
            for r in range(len(container)):
                Sum_comp+=container[r][j]
            Sum_comp-=container[i][j]
            if Sum_comp!=Sum_ref:
                flag+=1
        if flag==len(container[0]):
            return 'Impossible'
    return 'Possible'



s=[[0,2,1], [1, 1,1],[2,0,0]]
print(organizingContainers(s))
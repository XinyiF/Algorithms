# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    all_possible = [
        [8, 1, 6], [3, 5, 7], [4, 9, 2],
        [6, 1, 8], [7, 5, 3], [2, 9, 4],
        [4, 9, 2], [3, 5, 7], [8, 1, 6],
        [2, 9, 4], [7, 5, 3], [6, 1, 8],
        [8, 3, 4], [1, 5, 9], [6, 7, 2],
        [4, 3, 8], [9, 5, 1], [2, 7, 6],
        [6, 7, 2], [1, 5, 9], [8, 3, 4],
        [2, 7, 6], [9, 5, 1], [4, 3, 8]]

    j,res=0,[]
    while j<len(all_possible):
        cost=0
        for i in range(3):
            for k in range(3):
                cost+=abs(s[i][k]-all_possible[j][k])
            j+=1
        res.append(cost)
    return min(res)














s=[[5,3,4],[1,5,8],[6,4,2]]

print(formingMagicSquare(s))




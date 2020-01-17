#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
    count,rank,res={},1,[]
    for i in scores:
        if not i in count:
            count[i]=rank
            rank+=1
    s=len(scores)-1
    for j in alice:
        if j < scores[-1]:
            res.append(rank)
        elif j>scores[0]:
            res.append(1)
        else:
            while s >= 0:
                if j == scores[s]:
                    res.append(count[scores[s]])
                    break
                elif j<scores[s]:
                    res.append(count[scores[s]]+1)
                    break
                else:
                    s -= 1
    return res








s=[100 ,90 ,90 ,80, 75, 60]
a=[50 ,65, 77, 90, 102]

print(climbingLeaderboard(s,a))

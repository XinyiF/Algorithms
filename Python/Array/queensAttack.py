# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    total=r_q-1+n-r_q+c_q-1+n-c_q+min(n-r_q,n-c_q)+\
          min(c_q-1,n-r_q)+min(r_q-1,c_q-1)+min(r_q-1,n-c_q)
    if not obstacles:return total
    hor_larger,hor_smaller,vert_larger,vert_smaller=[0],[0],[0],[0]
    ru,lu,ll,rl=[0],[0],[0],[0]
    for i in range(k):
        r, c = obstacles[i][0], obstacles[i][1]
        diff_r, diff_c = r - r_q, c - c_q
        if r == r_q:
            if c < c_q:
                vert_smaller.append(c)
            else:
                vert_larger.append(n - c + 1)
        elif c == c_q:
            if r > r_q:
                hor_larger.append(n - r + 1)
            else:
                hor_smaller.append(r)
        elif diff_r > 0 and diff_r == diff_c:
            rl.append(min(n - r + 1, n - c + 1))
        elif diff_r > 0 and diff_c == -diff_r:
            lu.append(min(c, n - r + 1))
        elif diff_r < 0 and diff_r == diff_c:
            ll.append(min(r, c))
        elif diff_r < 0 and diff_c == -diff_r:
            rl.append(min(r, n - c + 1))
    return total-max(hor_larger)-max(hor_smaller)-max(vert_larger)-\
           max(vert_smaller)-max(ru)-max(lu)-max(ll)-max(rl)




ob=[[5,5],[4,2],[2,3],[1,3]]
print(queensAttack(5,3,4,3,ob))





def dfs(l, sum, time, tsum):
    global tot
    if sum + (totalAll - tsum) < tot:
        return
    if time > m:
        return
    if l == n:
        if tot < sum:
            tot = sum
    else:
        dfs(l + 1, sum + res[l][0], time + res[l][1], tsum + res[l][0])
        dfs(l + 1, sum, time, tsum + res[l][0])
if __name__=="__main__":
    n, m = map(int, input().split())
    res = []
    tot = 0
    totalAll = 0
    for _ in range(n):
        p = list(map(int, input().split()))
        totalAll += p[0]
        res.append(p)
    dfs(0, 0, 0, 0)
    print(tot)
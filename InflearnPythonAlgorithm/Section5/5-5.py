# 바둑이 승차
def DFS(L, sum, tsum):
    global res
    # Cut Edge Tech
    # tsum은 바둑이를 넣었든 안 넣었든 더해주는 값이고 total-tsum 한 값을 현재 sum에 넣어도 결과값보다 적으면 계산을 안하고 return
    if sum + (total-tsum) < res:
        return
    if sum > c:
        return
    if L == n:
        if res < sum:
            res = sum
    else:
        DFS(L + 1, sum + a[L], tsum + a[L])
        DFS(L + 1, sum, tsum + a[L])

if __name__=="__main__":
    c, n = map(int, input().split())
    a = []
    res = 0
    for _ in range(n):
        b = int(input())
        a.append(b)
    total = sum(a)
    DFS(0, 0, 0)
    print(res)
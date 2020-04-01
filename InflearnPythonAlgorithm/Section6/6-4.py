
def dfs(l, sum):
    global cnt
    if sum > T:
        return
    if l == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(a[l][1] + 1):
            dfs(l + 1, sum + (a[l][0] * i))

if __name__=="__main__":
    T = int(input())
    k = int(input())
    a = []
    for _ in range(k):
        pi, ni = map(int, input().split())
        a.append((pi, ni))
    a.sort(reverse=True)
    cnt = 0
    dfs(0, 0)
    print(cnt)

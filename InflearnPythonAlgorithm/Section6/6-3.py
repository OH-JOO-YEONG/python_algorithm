

def dfs(l, sum):
    if l == n:
        if sum > 0:
            x[sum] = 1
    else:
        dfs(l + 1, sum + s[l])
        dfs(l + 1, sum - s[l])
        dfs(l + 1, sum)


if __name__=="__main__":
    n = int(input())
    s = list(map(int, input().split()))
    total = sum(s)
    x = [0] * (total + 1) # 메모리가 20만이나 차지할 수 있음 비효율적
    dfs(0, 0)
    res = total - sum(x)
    print(res)

"""
정답지
def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L, sum + G[L])
        DFS(L, sum - G[L])
        DFS(L, sum)

n = input()
G = list(map(int, input().split()))
s = sum(G)
res = set()
DFS(0, 0)

"""

# 조합구하기

def DFS(L, s):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    if s > n:
        return
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, 1 + i)


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0, 1)
    print(cnt)




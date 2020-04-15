# 경로탐색(그래프 dfs)

def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0: # 경로를 찾고 방문이 체크됐는지 확인
                ch[i] = 1 # 방문체크
                path.append(i)
                dfs(i) # 그 경로로 감.
                path.pop()
                ch[i] = 0 # 다시 시스템스택에서 나올 때는 방문체크 풀어줌


if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    ch = [0] * (n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1
    path = []
    path.append(1)
    ch[1] = 1
    dfs(1)
    print(cnt)
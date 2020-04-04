def dfs(x, y):
    global cnt
    if x == ed[0] and y == ed[1]:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if mt[xx][yy] > mt[x][y]:
                    dfs(xx, yy)

if __name__=="__main__":
    n = int(input())
    mt = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    min1 = 214000000
    max1 = -214700000
    st = [0, 0]
    ed = [0, 0]
    for i in range(n):
        for j in range(n):
            tmp = mt[i][j]
            if min1 > tmp:
                min1 = tmp
                st[0] = i
                st[1] = j
            if max1 < tmp:
                max1 = tmp
                ed[0] = i
                ed[1] = j
    dfs(st[0], st[1])
    print(cnt)

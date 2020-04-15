# 단지번호붙이기(DFS, BFS)
def dfs(x, y):
    global cnt
    cnt += 1 # 발견했으니 카운트
    h[x][y] = 0 # 0으로 초기화
    for k in range(4): # 4방향탐색
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n and h[xx][yy] == 1: # 다음 갈려는 방향이 조건에 맞으면
            dfs(xx, yy)

if __name__=="__main__":
    n = int(input())
    h = [list(map(int, input())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []

    for i in range(n):
        for j in range(n):
            if h[i][j] == 1: # 탐색해서 1이면
                cnt = 0
                dfs(i, j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for q in res:
        print(q)

"""
BFS 방식
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
cnt = 0
res = []
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 0:
                        continue
                    board[x][y] = 0
                    Q.append((x, y))
                    cnt += 1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
"""
# 안전영역(BFS)
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
res = 0
dq = deque()

for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and board[i][j] > h:
                cnt += 1
                ch[i][j] = 1
                dq.append((i, j))
                while dq:
                    tmp = dq.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and ch[x][y] == 0 and board[x][y] > h:
                            ch[x][y] = 1
                            dq.append((x, y))
    res = max(res, cnt)

print(res)

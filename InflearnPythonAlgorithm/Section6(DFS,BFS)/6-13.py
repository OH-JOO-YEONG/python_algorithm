# 섬나라 아일랜드
from collections import deque
n = int(input())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
land = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            land[i][j] = 0
            dq.append((i, j))
            cnt += 1
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and land[x][y] == 1:
                        land[x][y] = 0
                        dq.append((x, y))

print(cnt)
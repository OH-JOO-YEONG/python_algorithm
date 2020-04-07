# 토마토(BFS)
# 파이참 컴파일러는 n, m 값이 너무 많다고 하는데 정답지는 맞다.. 뭐지?
import sys
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
m, n = map(int, sys.stdin.readline().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
dis = [[0] * m for _ in range(n)]
flag = 1
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))

while dq:
    tmp = dq.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        if 0 <= x < n and 0 <= y < m and tomato[x][y] == 0:
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            tomato[x][y] = 1
            dq.append((x, y))


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
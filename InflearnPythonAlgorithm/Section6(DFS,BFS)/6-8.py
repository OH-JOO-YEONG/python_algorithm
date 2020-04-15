# 사과나무(BFS)
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
dq = deque()
ch[n // 2][n // 2] = 1
res = a[n // 2][n // 2]
dq.append((n // 2, n // 2))
L = 0
while True:
    if L == n // 2:
        break
    size = len(dq)
    for i in range(size):
        tmp = dq.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                res += a[x][y]
                ch[x][y] = 1
                dq.append((x, y))

    L += 1

print(res)

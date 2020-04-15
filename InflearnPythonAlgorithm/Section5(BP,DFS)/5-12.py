# 인접행렬(가중치 방향그래프)

n, m = map(int, input().split())

a = [[0] * n for _ in range(n)]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]

for _ in range(m):
    x, y, g = map(int, input().split())
    a[x - 1][y - 1] = g

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
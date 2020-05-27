# 플로이드-와샬
n, m = map(int, input().split())
dis = [[5000] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dis[i][i] = 0

# 바로 직행했을 때의 값
for _ in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c

# 경유지 k를 거쳤을 때의 값 (플로이드 와샬 알고리즘)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dis[i][j] == 5000:
            print('M', end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
# 최대점수 구하기(냅색)

n, m = map(int, input().split())
# dy = [[0] * (m + 1) for _ in range(n + 1)]

# 2차원 배열로 하는법
# for i in range(1, n + 1):
#     pv, pt = map(int, input().split())
#     for k in range(0, m + 1):
#         dy[i][k] = dy[i - 1][k]
#     for j in range(pt, m + 1):
#         dy[i][j] = max(dy[i - 1][j - pt] + pv, dy[i][j])
#
# print(dy[n][m])

# 1차원 배열
dy = [0] * (m + 1)

for i in range(n):
    pv, pt = map(int, input().split())
    for j in range(m, pt - 1, -1):
        dy[j] = max(dy[j - pt] + pv, dy[j])
print(dy[m])
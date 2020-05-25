# 가방문제(냅색 알고리즘)

n, w = map(int, (input().split()))
dy = [0] * (w + 1)

for j in range(n):
    jw, jv = map(int, input().split())
    for k in range(jw, w + 1):
        tmp = dy[k - jw] + jv
        if tmp > dy[k]:
            dy[k] = tmp
print(dy[w])
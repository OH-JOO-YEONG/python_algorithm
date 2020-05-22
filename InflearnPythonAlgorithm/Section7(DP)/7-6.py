# 가장 높은 탑 쌓기
from operator import itemgetter
n = int(input())
arr = []
dy = [0] * (n + 1)
res = 0
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
arr.sort(reverse=True)
dy[1] = arr[0][1]
arr.insert(0, 0)
res = 0

for i in range(2, n + 1):
    cur = arr[i][1]
    max_h = 0
    for j in range(i - 1, 0, -1):
        if arr[j][2] > arr[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = cur + max_h
    res = max(res, dy[i])

print(res)
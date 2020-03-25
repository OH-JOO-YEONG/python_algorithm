# 격자판 최대합
n = int(input())
a = []
max_t = 0
ct = 0

# a = [list(map(int, input().split())) for _ in range(n)] ==
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    tot = 0
    if sum(a[i]) > max_t:
        max_t = sum(a[i])
    for j in range(n):
        tot += a[j][i]
        if tot > max_t:
            max_t = tot
        if i == 0:
            ct += a[j][j]
            if ct > max_t:
                max_t = ct
            ct = 0
            ct += a[j][n-j-1]
            if ct > max_t:
                max_t = ct

print(max_t)

"""
정답지
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 = a[i][i]
    sum2 = a[i][n - i - 1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)
"""



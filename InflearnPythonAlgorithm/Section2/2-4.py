"""
정렬된 리스트 합치는 법

"""

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []

p1, p2 = 0, 0

while True:
    if p1 == n:
        c = c + b[p2:]
        break
    elif p2 == m:
        c = c + a[p1:]
        break
    if a[p1] > b[p2]:
        c.append(b[p2])
        p2 += 1
    else:
        c.append(a[p1])
        p1 += 1

for i in c:
    print(i, end=' ')

"""
정답지
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []
p1=p2=0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
"""
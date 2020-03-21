from collections import deque

n = int(input())
a = list(map(int, input().split()))
a = deque(a)
res = []
lt = a[0]
rt = a[-1]
if lt < rt:
    s = a.popleft()
    res.append("L")
else:
    s = a.pop()
    res.append("R")

while True:
    lt = a[0]
    rt = a[-1]
    if s > lt and s > rt:
        break
    if lt > rt:
        if rt > s:
            s = a.pop()
            res.append("R")
        elif lt > s:
            s = a.popleft()
            res.append("L")
        else:
            break
    else:
        if lt == rt:
            a.pop()
            res.append("L")
            break
        if lt > s:
            s = a.popleft()
            res.append("L")
        elif rt > s:
            s = a.pop()
            res.append("R")
        else:
            break

print(len(res))
for i in res:
    print(i, end='')

"""
정답지

lt = 0
rt = n - 1
last = 0
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], "L"))
    if a[rt] > last:
        tmp.append((a[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
"""
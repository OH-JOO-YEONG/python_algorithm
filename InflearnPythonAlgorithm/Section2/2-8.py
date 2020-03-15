n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    x, y, z = map(int, input().split())
    if y == 0:
        for _ in range(z):
            a[x-1].append(a[x-1].pop(0))
    elif y == 1:
        for _ in range(z):
            a[x-1].insert(0, a[x-1].pop())

for x in a:
    print(x)

lt = 0
rt = n
res = 0
for i in range(n):
    for j in range(lt, rt):
        res += a[i][j]
    if i < n // 2:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1
print(res)
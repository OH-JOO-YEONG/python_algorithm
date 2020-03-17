n, m = map(int, input().split())

a = list(map(int, input().split()))

a.sort()
print(a)
x = 0
y = n - 1
while x <= y:
    mid = (x + y) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] < m:
        x = mid + 1
    else:
        y = mid - 1


# 주사위 게임
n = int(input())
max_t = 0

for i in range(n):
    a = list(map(int, input().split()))
    result = 0
    if a[0] == a[1] and a[1] == a[2]:
        result = a[0] * 1000 + 10000
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        if a[1] == a[2]:
            result = a[1] * 100 + 1000
        else:
            result = a[0] * 100 + 1000
    else:
        a_m = max(a)
        result = a_m * 100

    if max_t < result:
        max_t = result

print(max_t)
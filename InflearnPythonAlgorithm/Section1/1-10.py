n = int(input())
a = list(map(int, input().split()))
pre = 0
cnt = 0
res = 0

for i in range(len(a)):
    if pre != 0:
        if a[i] != 0:
            cnt += 1
    if a[i] == 0:
        cnt = 0
    res += a[i] + cnt
    pre = a[i]

print(res)

"""
정답지
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
"""
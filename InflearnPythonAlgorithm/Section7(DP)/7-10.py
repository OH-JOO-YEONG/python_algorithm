# 동전교환(냅색)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dy = [m + 1] * (m + 1) # j 원을 거슬러주는데 사용된 동전의 최소개수
dy[0] = 0

for i in range(n):
    for j in range(arr[i], m + 1):
        tmp = dy[j - arr[i]] + 1
        dy[j] = min(tmp, dy[j])

print(dy[m])
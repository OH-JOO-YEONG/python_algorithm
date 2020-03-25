# 마구간 정하기(결정 알고리즘) 이분탐색
n, c = map(int, input().split())

def Count(a):
    cnt = 1 # 놓여진 말 수
    s = magu[0] # 처음 놓여진 말의 좌표
    for i in magu:
        if i - s >= a: # 두 마굿간 인접의 거리가 a 보다 크면
            s = i
            cnt += 1
    return cnt

magu = []
res = 0

for _ in range(n):
    tmp = int(input())
    magu.append(tmp)

magu.sort()

# 기준을 마구간 거리의 사잇값을 한다. 최소는 당연히 1이겠고 최대는 최대로 큰 수
lt = 1
rt = magu[n - 1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c: # 좌표 안에 말이 놓여진 수가 c보다 크면
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

# 랜선자르기(결정알고리즘) 이분탐색
k, n = map(int, input().split())
Line = []
res = 0
largest = 0

# 이분탐색 이용하는 문제
# 오답문제니 다시 습득하길 바람!

def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp) # max 함수는 ()값 안에 중에 제일 큰 수 변수에 넣기

lt = 1
rt = largest # 답의 최대길이는 당연히 입력의 가장 큰 수

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n: # Count 함수에서 리턴된 값이 n 보다 크면 결과값 정하고 lt 다시 정하고 while문 시작
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)

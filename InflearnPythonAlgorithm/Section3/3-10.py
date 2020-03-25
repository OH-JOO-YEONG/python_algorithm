# 역수열(그리디)
n = int(input())
r = list(map(int, input().split()))
zero = [0] * n

for i in range(n):
    cnt = 0
    x = 0
    key = 0
    while cnt <= r[i]:
        if zero[key] == 0:
            cnt += 1
        if zero[key] != 0:
            x += 1
        key += 1

    zero[cnt - 1 + x] = i + 1

for i in zero:
    print(i, end=' ')

"""
미친정답지 - 질문상세 내용
N부터 처리한다는 것은 ans에 이미 들어가 있는 숫자는 현재 처리하려는 
숫자보다 모두 크다는 것이므로 현재 처리하려는 숫자가 x번 index로 insert되면 
자기 앞에 무조건 큰 숫자가 x개 생기고 현재 숫자 다음에 처리되는 숫자들은 자기보다 
작기때분에 어디에 insert 되도 상관없습니다.

n = int(input())

a = list(map(int, input().split()))

a = a[::-1]

ans = []

print(a)

for x in a:
    ans.insert(x, n)
    n -= 1
    print(x)
    print(ans)

print(ans)

"""

"""
정답지
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0: # a[i] 값이 밑에 조건에 의해 계속 빼져서 0이 되고 j가 계속 증가하는데 seq[j]의 값이 0이면 seq[j] = i + 1을 넣어준다
        # 조건에서 a[i] == 0 의 의미는 이 앞에 빈 공간을 확보했다는 것 seq[j] == 0 의 의미는 빈공간 확보
        하고나서 자기보다 작은 숫자가 공간을 확보하고 있을 수 있으니 j가 증가하면서 빈공간에 저장
            seq[j] = i + 1
            break
        elif seq[j] == 0: # seq[j]의 값이 0을 만나면 본래 a[i] 값을 계속 빼줘라
            a[i] -= 1

for i in seq:
    print(i, end=' ')
"""

"""
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
"""

import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

a = []
cnt = [0 for _ in range(n + m)]
result = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
            a.append(i + j) # 보완할 점 a라는 리스트에 메모리를 더 씀.

for k in a:
    cnt[k - 1] += 1 # 반복문을 한번 더 돌림

for o in range(len(cnt)):
    if cnt[o] == max(cnt):
        result.append(o + 1) # result라는 리스트를 씀 답지는 result라는 변수만 썼는데. 메모리 차이 좀 있음.

for l in result:
    print(l, end=" ")

# 정답지
"""
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=" ")
"""
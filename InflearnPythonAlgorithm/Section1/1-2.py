# K번째 작은 수
"""
K번째 작은수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수 중
k번째로 작은 수를 출력하는 프로그램을 작성하세요.
"""

import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1 : e]
    a.sort()
    print(f"#{t + 1} {a[k - 1]}")



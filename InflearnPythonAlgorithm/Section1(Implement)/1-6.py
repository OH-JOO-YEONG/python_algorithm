"""
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.
못풀었던 문제 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 다시한번 보자!
"""
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
result = 0
max = 0
def digit_sum(x):
    sum_x = 0
    while x > 0:
        sum_x += x % 10
        x = x // 10
    return sum_x

for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        result = x
print(result)

# 쉬운 정답지
"""
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
"""
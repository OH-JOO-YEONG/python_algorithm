"""
대표값
N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일
경우 번호가 빠른 학생의 번호를 답으로 한다.
"""


# import sys
# sys.stdin = open("input.txt", "rt")
# """
# 평균에 가까운 학생 - 평균값에서 현재값 뺀 절대값이 가장 작은 값
# 답이 2개일 경우 성적이 높은 학생의 번호 - 소팅해서 위에 평균에 가까운 학생을 찾고 그 값을 원래 리스트에서에 인덱스를 찾는다
# """
# n = int(input())
# s = list(map(int, input().split()))
# a_s = int(round(sum(s) / n))
# min_s = []
# sort_s = sorted(s)
# max_s = 0
#
# for i in range(n):
#     min_s.append(a_s - sort_s[i])
#     if max_s <= a_s - abs(min_s[i]):
#         max_s = a_s - abs(min_s[i])
#         cnt = i
#
# print(a_s, s.index(sort_s[cnt]) + 1)

# # 정답지
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
min = 10000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1

    elif tmp == min: # 답이 두개일 경우 성적이 높은 학생의 번호 출력조건
        if x > score: # 답이 되는 점수가 여러개 일 경우 이 조건에서 걸러짐
            score = x
            res = idx + 1
    print(res)
print(ave, res)


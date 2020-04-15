# 숫자만 추출
import re

n = input()

number = re.findall("\d", n)
j = ""
cnt = 0
# 0이 아닌 수를 만나기전 까지의 0은 무시

for i in number:
    if i == '0' and cnt == 0:
        pass
    else:
        j = j + i
        cnt += 1
res = int(j)
print(res)
cnt = 0

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)

"""
정답지
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
"""
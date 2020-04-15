# 아나그램(딕셔너리 해쉬)
s1 = input()
s2 = input()

ana1 = dict()
ana2 = dict()

for w in s1:
    if w in ana1:
       ana1[w] += 1
    else:
        ana1[w] = 1

for w in s2:
    if w in ana2:
       ana2[w] += 1
    else:
        ana2[w] = 1

p = sorted(ana1)
if sorted(ana2) != sorted(ana1):
    print("NO")
else:
    for i in p:
        if ana1[i] != ana2[i]:
            print("NO")
            break
    else:
        print("YES")

"""
정답지
"""
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    # 키가 있을 때는 해당 키의 값을 반환하지만 키가 없을 때는 기본값을 반환한다.
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

if str1 == str2: # key값과 value값이 같으면 true를 리턴
    print("YES")
else:
    print("NO")
# 아나그램(리스트 해쉬)
a = input()
b = input()

a = list(a)
b = list(b)

a.sort()
b.sort()

if a == b:
    print("YES")
else:
    print("NO")

"""
정답지 
C++ 형식으로 코딩하는 법
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    if x.islower():
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    if x.islower():
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
"""

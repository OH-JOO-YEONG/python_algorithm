# 단어찾기(해쉬)
n = int(input())

a = []

for _ in range(n):
    s = input()
    a.append(s)

for _ in range(n - 1):
    s = input()
    a.remove(s)

print(a[0])

"""
정답지

n = input()
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
"""
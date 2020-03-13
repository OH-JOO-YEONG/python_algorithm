n = int(input())

def palindrome(x):
    x = x.lower()
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


for i in range(n):
    s = input()
    if palindrome(s):
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')

"""
미친정답지
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')
"""

"""  
정답지

for i in range(n):
    s = input()
    s = s.upper()
    for j in range(len(s) // 2):
        if s[j] != s[-1-j]:
            print(f'#{i + 1} NO')
            break
    else:
        print(f'#{i + 1} YES')
"""


n = int(input())

arr = list(map(int, input().split()))

def reverse(x):
    x = list(str(x))
    list_x = ""
    cnt = 0
    for i in range(len(x) - 1, -1, -1):
        if cnt == 0 and int(x[i]) == 0:
            continue
        cnt += 1
        list_x += x[i]

    return int(list_x)

"""
정답지
def reverse1(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
"""

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True

for i in arr:
    if isPrime(reverse(i)):
        print(reverse(i), end=' ')
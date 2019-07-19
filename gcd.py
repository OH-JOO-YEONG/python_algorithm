#최대공약수 구하기 알고리즘
def gcd(a, b):
    i = min(a, b)
    while True:
        if (a % i == 0) and (b % i == 0):
            return i
        i = i - 1

print(gcd(10, 12))
print(gcd(3, 6))
print(gcd(60, 24))

#유클리드 최대공약수 알고리즘
#a 와 b는 최대공약수 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같습니다.
#어떤 수와 0의 최대공약수는 자기 자신
def ugcd(a, b):
    print(a, b)
    if b == 0:
        return a
    return ugcd(b, a % b)

print(ugcd(10, 12))

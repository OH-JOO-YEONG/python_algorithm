
#연속한 숫자의 곱을 구하는 알고리즘

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i

    return f

print(fact(2))
print(fact(5))
print(fact(10))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(2))
print(factorial(5))
print(factorial(10))

#연습문제1
#1부터 n까지의 합 구하기를 재귀호출

def factsum(n):
    if n <= 1:
        return 1
    return n + factsum(n - 1)

print(factsum(10))

#연습문제2
#숫자 n개 중에서 최댓값 찾기를 재귀호출

def maxfact(a, n):
    if n == 1:
        return a[0]
    max_n_1 = maxfact(a, n - 1) # 맨 처음 a[0]까지 가고 아래에서 비교하면서 올라오는 재귀
    # print(max_n_1)
    if max_n_1 > a[n - 1]:
        return max_n_1
    else:
        return a[n - 1]

v = [17, 18, 33, 58, 7, 33, 42, 92]
print(maxfact(v, len(v)))


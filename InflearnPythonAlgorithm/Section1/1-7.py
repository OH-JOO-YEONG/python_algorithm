"""
소수의 개수(에라토스테네스의 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.
"""
"""
팁

"""

n = int(input())

def prime(n):
    if n <= 1:
        return 0
    cnt = 0
    list_n = [0] * (n + 1)
    for i in range(2, len(list_n)):
        if list_n[i] == 0:
            cnt += 1
        for j in range(i, n + 1, i):
            list_n[j] = 1
    return cnt

print(prime(n))

"""
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
    """

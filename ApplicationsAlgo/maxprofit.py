#최대 수익을 구하는 알고리즘

def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

'''
1. 최대 수익을 저장하는 변수를 만들고 0을 저장합니다.
2. 지금까지의 최저 주가를 저장하는 변수를 만들고 첫째 날의 주가를 기록합니다.
3. 둘째 날의 주가부터 마지막 날의 주가까지 반복합니다.
4. 반복하는 동안 그날의 주가에서 최저 주가를 뺀 값이 현재 최대 수익보다 크면 최대 수익 값을 그 값으로 고칩니다.
5. 그날의 주가가 최저 주가보다 낮으면 최저 주가 값을 그날의 주가로 고칩니다.
6. 처리할 날이 남았으면 4번 과정으로 돌아가 반복하고, 다 마쳤으면 최대 수익에 저장된 값을 결괏값으로 돌려주고 종료합니다.
'''

def max_profit2(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

print(max_profit2(stock))
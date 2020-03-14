def reverse(x):
    a = [0] * len(x)
    for i in range(1, len(x) + 1):
        a[-i] = x[i - 1]
    return a

arr = list(range(1, 21))
for _ in range(10):
    a, b = map(int, input().split())
    arr[a-1:b] = reverse(arr[a-1:b])

for i in arr:
    print(i, end=' ')

"""
정답지
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]
        
a.pop(0)
for x in a:
    print(x, end=' ')
"""
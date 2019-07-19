#동명이인을 찾는 알고리즘

def find_same_name(a):
    n = len(a)
    result = set()

    for i in range(0, n-1): # n-1인 이유 a[n-1] 은 이미 앞에서 다른 자료와 한번씩 다 비교했으므로 제외.
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])

    return result

name1 = ["Tom", "Mike", 'Jerry', 'Tom']
print(find_same_name(name1))
name2 = ["Tom", "Mike", 'Jerry', 'Tom', "Mike"]
print(find_same_name(name2))

#1 + 2 + 3 + ~~~ + n - 1 = (n-1)(n-1+1)/2 = n^2/2-n/2
#시간 복잡도 O(n^2)

#연습문제
#n명 중 두명을 뽑아 짝을 짓는다고 할때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보세요.
def matching_pairs(a):
    n = len(a)

    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

name1 = ["Tom", "Mike", 'Jerry']
print(matching_pairs(name1))
name2 = ["Tom", "Mike", 'Jerry', 'John', "Insang"]
print(matching_pairs(name2))
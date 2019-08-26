# practice 15-1
# 1.앞으로 처리할 사람을 저장할 큐를 만듭니다.
# 2.이미 큐에 추가한 사람을 저장할 집합을 만듭니다.
# 3.검색의 출발점이 될 사람을 큐와 집합에 추가합니다.
# 4.큐에 사람이 남아 있다면 큐에서 처리할 사람을 꺼냅니다.
# 5.꺼낸 사람을 출력합니다.
# 6.꺼낸 사람의 친구들 중 아직 큐에 추가된 적이 없는 사람을 골라 큐와 집합에 추가합니다.
# 7.큐에 처리할 사람이 남아 있다면 4번 과정부터 다시 반복합니다.

def graphsearch(a, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in a[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

number_info = {
    1 : [2, 3],
    2 : [4, 5],
    3 : [1],
    4 : [2],
    5 : [2]
}

graphsearch(number_info, 1)
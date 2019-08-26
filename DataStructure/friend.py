# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 1.앞으로 처리할 사람을 저장할 큐를 만듭니다.
# 2.이미 큐에 추가한 사람을 저장할 집합을 만듭니다.
# 3.검색의 출발점이 될 사람을 큐와 집합에 추가합니다.
# 4.큐에 사람이 남아 있다면 큐에서 처리할 사람을 꺼냅니다.
# 5.꺼낸 사람을 출력합니다.
# 6.꺼낸 사람의 친구들 중 아직 큐에 추가된 적이 없는 사람을 골라 큐와 집합에 추가합니다.
# 7.큐에 처리할 사람이 남아 있다면 4번 과정부터 다시 반복합니다.

# 입력 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)
    print(qu)
    print(done)
    while qu:
        p = qu.pop(0)
        print("---")
        print("qu:", qu)
        print("done:", done)
        print("p:", p) # 친구리스트 출력하는 곳
        print("1---")
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
                print("---")
                print("qu:", qu)
                print("done:", done)
                print("2---")

# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구 리스트에도 A가 나옴

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Tom')

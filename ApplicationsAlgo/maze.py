def solve_maze(g, start, end):
    qu = [] # 기억 장소 1: 앞으로 처리해야할 이동 경로를 큐에 저장
    done = set() # 기억 장소 2: 이미 큐에 추가한 꼭짓점들을 집합에 기록

    qu.append(start)
    done.add(start)

    while qu: #큐에 처리할 경로가 남아있으면
        p = qu.pop(0) # 큐에서 처리 대상을 꺼냄
        v = p[-1] # 큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야할 꼭짓점
        print('---')
        print('p :', p)
        print('v :', v)
        if v == end: # 처리해야할 꼭짓점이 도착점이면 종료
            return p #지금까지의 전체 이동 경로를 돌려주고 종료
        for x in g[v]: # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 꼭짓점을
                qu.append(p + x) # 이동 경로에 새 꼭짓점으로 추가하여 큐에 저장하고
                done.add(x) #집합에도 추가
                print('qu: ', qu)



    return "?"

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

print(solve_maze(maze, 'a', 'p'))
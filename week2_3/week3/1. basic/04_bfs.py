"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bad_bfs(graph, start):
    # deque를 사용하지 않음
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []
    temp = []

    temp.append(start)

    while len(temp) != 0:
        step = temp[0]
        for i in graph[step]:
            if i not in visited and i not in temp: # in 방식은 시간 복잡도가 O(N)이기 때문에, 비효율적이다.
                temp.append(i)
        visited.append(temp.pop(0)) # pop(0): Python 리스트에서 첫 번째 원소를 제거한 뒤 나머지 원소들을 앞으로 이동시켜야 하기 때문에 O(N)의 복잡도
        
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    check = { start } # 방문 여부를 체크하기 위한 set. in 연산을 할때 더 효율적인 시간 복잡도를 가짐

    while queue: 
        current = queue.popleft() #popleft를 사용해 제일 왼쪽의 원소를 꺼내줌
        visited.append(current)

        for i in graph[current]:
            if i not in check:
                queue.append(i)
                check.add(i)

    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


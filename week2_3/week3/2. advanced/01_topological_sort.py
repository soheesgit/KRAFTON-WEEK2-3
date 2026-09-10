"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    result = []
    dic = {}

    # 빈 딕셔너리 생성
    for i in range(vertices):
        dic[i] = []

    # 진입 차수를 담을 배열 생성
    indegrees = [0] * vertices

    # 딕셔너리, 진입 차수 데이터 채우기
    for first, second in edges:
        dic[first].append(second)
        indegrees[second] += 1

    queue = deque()

    # 진입차수가 0이라면 큐에 넣기
    for i in range(vertices):
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        num = queue.popleft() # 큐의 맨 앞인 숫자를 꺼낸다.
        result.append(num)

        # 현재 정점에서 나가는 간선을 제거한 것으로 처리
        for i in dic[num]:
            indegrees[i] -= 1 
            
            # 새로운 진입 차수가 0이 되면 큐에 삽입
            if indegrees[i] == 0:
                queue.append(i)

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

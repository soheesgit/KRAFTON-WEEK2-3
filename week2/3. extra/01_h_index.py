"""
[정렬 - H-Index]

문제:
- LeetCode 274. H-Index
- https://leetcode.com/problems/h-index/

문제 설명:
- citations[i]는 i번째 논문이 인용된 횟수를 의미합니다.
- h-index는 최소 h번 이상 인용된 논문이 최소 h개 존재하는
  가장 큰 h 값입니다.

입력:
- citations: 각 논문의 인용 횟수를 담은 정수 리스트

출력:
- 연구자의 h-index

예제 1:
입력: [3, 0, 6, 1, 5]
출력: 3

설명:
- 내림차순 정렬하면 [6, 5, 3, 1, 0]
- 3편의 논문이 각각 최소 3번 이상 인용되었습니다.
- 따라서 h-index는 3입니다.

예제 2:
입력: [1, 3, 1]
출력: 1

풀이:
- 인용 횟수를 내림차순으로 정렬합니다.
- i번째 논문까지 확인했을 때 논문의 개수는 i + 1개입니다.
- citations[i] >= i + 1 이라면,
  최소 i + 1번 이상 인용된 논문이 i + 1개 존재합니다.
- 조건을 만족하지 않는 순간 반복을 종료합니다.

시간 복잡도:
- 정렬: O(n log n)
- 탐색: O(n)
- 전체: O(n log n)
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)
        h = 0

        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                h = i + 1
            else:
                break

        return h


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    citations1 = [3, 0, 6, 1, 5]
    print(solution.hIndex(citations1))  # 3

    citations2 = [1, 3, 1]
    print(solution.hIndex(citations2))  # 1
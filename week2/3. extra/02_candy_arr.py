```python
"""
[그리디 - Candy]

문제:
- LeetCode 135. Candy
- https://leetcode.com/problems/candy/

문제 설명:
- n명의 아이가 일렬로 서 있고, 각 아이는 rating을 가지고 있습니다.
- 모든 아이는 최소 1개의 사탕을 받아야 합니다.
- 이웃보다 rating이 높은 아이는 그 이웃보다 더 많은 사탕을 받아야 합니다.
- 조건을 만족하면서 필요한 최소 사탕의 개수를 구합니다.

입력:
- ratings: 각 아이의 평점을 담은 정수 리스트

출력:
- 필요한 최소 사탕의 총 개수

예제 1:
입력: [1, 0, 2]
출력: 5

설명:
- 사탕을 [2, 1, 2]개씩 나누어 줄 수 있습니다.

예제 2:
입력: [1, 2, 2]
출력: 4

설명:
- 사탕을 [1, 2, 1]개씩 나누어 줄 수 있습니다.

풀이:
- 모든 아이에게 우선 사탕을 1개씩 줍니다.
- 왼쪽에서 오른쪽으로 순회하며,
  현재 아이의 rating이 왼쪽 아이보다 높다면
  왼쪽 아이보다 사탕을 1개 더 줍니다.
- 이후 오른쪽에서 왼쪽으로 다시 순회하며,
  현재 아이의 rating이 오른쪽 아이보다 높다면
  오른쪽 아이보다 최소 1개 더 많은 사탕을 줍니다.
- 이때 첫 번째 순회에서 이미 정해진 사탕 개수를 유지해야 하므로
  현재 값과 오른쪽 아이 + 1 중 최댓값을 사용합니다.

시간 복잡도:
- 왼쪽 -> 오른쪽 순회: O(n)
- 오른쪽 -> 왼쪽 순회: O(n)
- 전체: O(n)

공간 복잡도:
- 사탕 개수를 저장하는 리스트: O(n)
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [1] * len(ratings)

        # 왼쪽 -> 오른쪽
        for i in range(1, len(ratings)):
            # 현재 아이의 평점이 왼쪽 아이보다 높다면
            if ratings[i] > ratings[i - 1]:
                # 왼쪽 아이보다 사탕을 하나 더 줌
                candies[i] = candies[i - 1] + 1

        # 오른쪽 -> 왼쪽
        for i in range(len(ratings) - 2, -1, -1):
            # 현재 아이의 평점이 오른쪽 아이보다 높다면
            if ratings[i] > ratings[i + 1]:
                # 기존 값과 오른쪽 아이보다 하나 많은 값 중 최댓값
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# 테스트
if __name__ == "__main__":
    solution = Solution()

    print(solution.candy([1, 0, 2]))  # 5
    print(solution.candy([1, 2, 2]))  # 4
    print(solution.candy([29, 51, 87, 87, 72, 12]))  # 12
```
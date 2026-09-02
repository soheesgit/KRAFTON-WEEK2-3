"""
[백트래킹 - Permutations]

문제:
- LeetCode 46. Permutations
- https://leetcode.com/problems/permutations/

문제 설명:
- 서로 다른 정수로 이루어진 nums가 주어집니다.
- nums로 만들 수 있는 모든 순열을 반환합니다.

입력:
- nums: 서로 다른 정수를 담은 리스트

출력:
- nums로 만들 수 있는 모든 순열

예제 1:
입력: [1, 2, 3]
출력: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

설명:
- [1, 2, 3]으로 만들 수 있는 모든 순서를 반환합니다.
- 총 3! = 6개의 순열이 존재합니다.

예제 2:
입력: [0, 1]
출력: [[0, 1], [1, 0]]

풀이:
- 백트래킹을 사용하여 모든 순열을 탐색합니다.
- current_arr에는 현재까지 선택한 숫자를 저장합니다.
- 이미 current_arr에 존재하는 숫자는 다시 선택하지 않습니다.
- 숫자를 하나 선택한 뒤 재귀 호출을 통해 다음 숫자를 선택합니다.
- current_arr의 길이가 nums의 길이와 같아지면 완성된 순열을 answer에 추가합니다.
- 재귀가 끝나면 pop()을 통해 마지막으로 선택한 숫자를 제거하고 다른 경우를 탐색합니다.

시간 복잡도:
- 만들 수 있는 순열의 개수: n!
- 각 순열을 복사하는 데 O(n)
- 전체: O(n × n!)
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []

        def backtracking(current_arr):
            # base condition
            if len(current_arr) == len(nums):
                answer.append(current_arr[:])
                return

            for i in range(len(nums)):
                if nums[i] in current_arr:
                    continue

                current_arr.append(nums[i])
                backtracking(current_arr)
                current_arr.pop()

        backtracking([])
        return answer

class fest_Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        answer = []
        used = [False] * len(nums)
        
        def backtracking(current_arr):
            # base condition
            if len(current_arr) == len(nums):
                answer.append(current_arr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current_arr.append(nums[i])
                backtracking(current_arr)
                used[i] = False
                current_arr.pop()

        backtracking([])
        return answer
    
# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3]
    print(solution.permute(nums1))
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3],
    #  [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    nums2 = [0, 1]
    print(solution.permute(nums2))
    # [[0, 1], [1, 0]]
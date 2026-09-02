"""
[백트래킹 - Permutations II]

문제:
- LeetCode 47. Permutations II
- https://leetcode.com/problems/permutations-ii/

문제 설명:
- 중복된 숫자를 포함할 수 있는 nums가 주어집니다.
- nums로 만들 수 있는 모든 서로 다른 순열을 반환합니다.

입력:
- nums: 중복된 값을 포함할 수 있는 정수 리스트

출력:
- nums로 만들 수 있는 중복 없는 모든 순열

예제 1:
입력: [1, 1, 2]
출력: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

설명:
- 인덱스를 기준으로 가능한 모든 순열을 생성합니다.
- 생성된 인덱스를 실제 nums의 값으로 변환합니다.
- 중복된 결과를 제거하여 서로 다른 순열만 반환합니다.

예제 2:
입력: [1, 2, 3]
출력: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

풀이:
- 백트래킹을 사용하여 nums의 인덱스로 만들 수 있는 모든 순열을 생성합니다.
- current_arr에는 현재까지 선택한 인덱스를 저장합니다.
- 이미 current_arr에 존재하는 인덱스는 다시 선택하지 않습니다.
- 완성된 인덱스 순열을 nums의 실제 값으로 변환하여 real_answer를 만듭니다.
- real_answer를 순회하면서 unique에 없는 순열만 추가합니다.
- 최종적으로 중복이 제거된 unique를 반환합니다.

시간 복잡도:
- 인덱스 순열 생성: O(n × n!)
- 실제 값으로 변환: O(n × n!)
- 중복 제거: 최악의 경우 O(n × (n!)²)
- 전체: O(n × (n!)²)
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []

        def backtracking(current_arr):
            if len(current_arr) == len(nums):
                answer.append(current_arr[:])
                return

            for i in range(len(nums)):
                if i in current_arr:
                    continue
                current_arr.append(i)
                backtracking(current_arr)
                current_arr.pop()

        backtracking([])

        real_answer = [[nums[i] for i in x] for x in answer]


        unique = []

        for x in real_answer:
            if x not in unique:
                unique.append(x)

        return unique

    def best_result(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        answer = []
        used = [False] * len(nums)
        nums.sort() # 중복 제거에 용이하게 정렬

        def backtracking(current_arr):
            if len(current_arr) == len(nums):
                answer.append(current_arr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # 같은 깊이에서 같은 숫자를 다시 선택하지 않음
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
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

    nums1 = [1, 1, 2]
    print(solution.permuteUnique(nums1))
    # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    nums2 = [1, 2, 3]
    print(solution.permuteUnique(nums2))
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3],
    #  [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


# bruteforce
class Solution_1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rectangle = heights[0]
        for i in range(len(heights)):
            stack = [heights[i]]
            for j in range(i + 1, len(heights)):
                stack.append(heights[j])
                max_rectangle = max(max_rectangle, self.get_max_from_stack(stack))

        return max_rectangle

    def get_max_from_stack(self, stack):
        max_rectangle, highest_col, sm_col = stack[0], stack[0], stack[0],
        for i in range(1, len(stack)):
            highest_col = max(highest_col, stack[i])
            sm_col = min(sm_col, stack[i])
            max_rectangle = max(max_rectangle, highest_col, sm_col * (i + 1))

        return max_rectangle


# разбор решение от NeetCode
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pairs (idx, heights)
        max_area = 0
        for i, h in enumerate(heights):
            start_idx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start_idx = idx
            stack.append((start_idx, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


if __name__ == '__main__':
    s = Solution()
    test_case = [1, 2, 3]  # 4
    # test_case = [2, 4]  # 4
    # test_case = [2, 1, 5, 6, 2, 3]  # 10
    # test_case = [5, 6, 2]  # 10
    # test_case = [1]  # 1
    print(s.largestRectangleArea(test_case))



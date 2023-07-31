# https://leetcode.com/problems/trapping-rain-water/
from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_list, max_right_list = deque(), deque()
        max_left_list.append(0)
        max_right_list.append(0)

        for i in range(1, len(height)):
            left_max = max(height[i - 1], max_left_list[-1])
            max_left_list.append(left_max)

        for i in range(len(height) - 2, -1, -1):
            right_max = max(height[i + 1], max_right_list[0])
            max_right_list.appendleft(right_max)

        units = 0
        for i in range(1, len(height)):
            l, r = max_left_list[i], max_right_list[i]
            current_units = min(l, r) - height[i]
            if current_units > 0:
                units += current_units

        return units


if __name__ == '__main__':
    # test_case = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    test_case = [4, 2, 0, 3, 2, 5]  # 9
    solution = Solution()
    print(solution.trap(test_case))

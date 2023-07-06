# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_container = 0
        while l < r:
            current_container = (r - l) * min(height[l], height[r])
            max_container = max(current_container, max_container)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_container


if __name__ == '__main__':
    test_case = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
    s = Solution()
    print(s.maxArea(test_case))


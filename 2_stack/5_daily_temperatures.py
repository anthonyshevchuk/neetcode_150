# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # (idx, t)
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_idx, _ = stack.pop()
                diff = idx - prev_idx
                res[prev_idx] = diff
            stack.append((idx, t))
        return res


if __name__ == '__main__':
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [30, 40, 50, 60]
    # temperatures = [30, 20, 10, 0]
    print(Solution().dailyTemperatures(temperatures))
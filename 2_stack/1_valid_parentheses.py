# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'}': '{', ')': '(', ']': '['}

        for c in s:
            # open
            if c in lookup.values():
                stack.append(c)
            # close: previous must be the same and stack must not be empty
            else:
                if stack and stack[-1] == lookup[c]:
                    stack.pop(-1)
                else:
                    return False

        return False if stack else True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('{[}]'))


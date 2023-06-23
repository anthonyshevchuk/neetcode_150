# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.gen_next('(', 1, 0, n)
        return self.res

    def gen_next(self, partnthesis_str, open_count, close_count, n):
        if close_count == open_count:
            if open_count == close_count == n:
                self.res.append(partnthesis_str)

            elif open_count < n:
                self.gen_next(partnthesis_str + '(', open_count + 1, close_count, n)

        elif close_count < open_count:
            if open_count < n:
                self.gen_next(partnthesis_str + '(', open_count + 1, close_count, n)

            if close_count < n:
                self.gen_next(partnthesis_str + ')', open_count, close_count + 1, n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(1))



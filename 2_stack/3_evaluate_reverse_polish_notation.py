# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        for tok in tokens:
            if tok not in self.operators:
                self.stack.append(int(tok))
            else:
                self.run_operation(tok)

        return self.stack[-1]

    def run_operation(self, operation):
        res = 0
        if operation == '+':
            res = self.stack[-2] + self.stack[-1]
        elif operation == '-':
            res = self.stack[-2] - self.stack[-1]
        elif operation == '*':
            res = self.stack[-2] * self.stack[-1]
        elif operation == '/':
            res = self.stack[-2] / self.stack[-1]
            res = self.trunc_to_zero(res)

        for _ in range(2):
            self.stack.pop()
        self.stack.append(res)

    def trunc_to_zero(self, value):
        if value > 0:
            return int(value // 1)
        else:
            value *= -1
            value = value // 1
            return int(value * -1)


if __name__ == '__main__':
    # test_case = ["2", "1", "+", "3", "*"]  # 9
    test_case = ["4", "13", "5", "/", "+"]  # 6
    # test_case = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # 22
    # test_case = ["4", "-2", "/", "2", "-3", "-", "-"]  # -7
    solution = Solution()
    print(solution.evalRPN(test_case))

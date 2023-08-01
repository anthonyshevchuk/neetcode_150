# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def calculate(self, s: str) -> int:
        res, cur, prev = 0, 0, 0
        cur_operation = '+'

        i = 0
        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_operation == '+':
                    res += cur
                    prev = cur

                elif cur_operation == '-':
                    res -= cur
                    prev = -cur

                elif cur_operation == '*':
                    res -= prev
                    res += prev * cur
                    prev = prev * cur

                elif cur_operation == '/':
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)

                cur = 0

            elif cur_char != ' ':
                cur_operation = s[i]

            i += 1

        return res

if __name__ == '__main__':
    s = "3+2*2"
    solution = Solution()
    print(solution.calculate(s))



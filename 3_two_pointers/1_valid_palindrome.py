class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            while not s[p1].isalnum() and p1 < p2:
                p1 += 1

            while not s[p2].isalnum() and p1 < p2:
                p2 -= 1

            if s[p1].lower() != s[p2].lower():
                return False

            p1 += 1
            p2 -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    # test_case = 'cattac'
    # test_case = 'cat tac'
    test_case = 'Cat tac!'
    # test_case = "A man, a plan, a canal: Panama"
    # print("".join([c.lower() for c in test_case if c.isalnum()]))
    print(solution.isPalindrome(test_case))


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices) - 1):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > 0:
#                     max_profit = max(max_profit, profit)
#
#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for l in range(len(prices) - 1):
            r = l + 1
            while r <= len(prices) - 1 and prices[r] - prices[l] > 0:
                res = max(res, prices[r] - prices[l])
                r += 1
        return res


if __name__ == '__main__':
    s = Solution()
    test_case = [7, 1, 5, 3, 6, 4]  # 5
    # test_case = [7, 6, 4, 3, 1]  # 0
    print(s.maxProfit(test_case))
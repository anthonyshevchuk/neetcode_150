# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        count2nums = [[] for i in range(len(nums) + 1)]

        # запомним распределение чисел
        for num in nums:
            freq[num] += 1

        # заполним массив count2nums
        for key, v in freq.items():
            count2nums[v].append(key)

        res = []
        for i in range(len(count2nums) - 1, 0, -1):
            for n in count2nums[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))

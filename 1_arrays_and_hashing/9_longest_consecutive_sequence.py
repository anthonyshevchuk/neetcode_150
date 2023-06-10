from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            # check if it's a start of a sequence
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1

                max_length = max(length, max_length)

        return max_length

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2, 5]  # 5
    # nums = [100, 4, 200, 1, 3, 2]  # 4
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # 9
    # nums = [0, 3, 7, 2, 5, 8, 4]  # 4
    solution = Solution()
    print(solution.longestConsecutive(nums))

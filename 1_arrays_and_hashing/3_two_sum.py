# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            else:
                lookup[num] = i


if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))

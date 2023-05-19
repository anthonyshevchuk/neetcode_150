# https://leetcode.com/problems/contains-duplicate/


class Solution(object):
    def containsDuplicate(self, nums):  # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = {}
        for num in nums:
            if num not in lookup:  # O(1), since it's a hash table
                lookup[num] = num
            else:
                return True

        return False


if __name__ == "__main__":
    # nums = [1, 2, 3, 1]
    nums = [1, 2, 3, 6, 8]

    print(Solution().containsDuplicate(nums))

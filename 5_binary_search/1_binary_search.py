from typing import List

# recursive solution
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) == 0:
#             return -1
#
#         else:
#             l, r = 0, len(nums) - 1
#             return self.rec(nums, l, r, target)
#
#     def rec(self, nums, l, r, target):
#         if l == r:
#             if target == nums[l]:
#                 return l
#             else:
#                 return -1
#         else:
#             split_idx = (r - l + 1) // 2 + l  # split_idx = 1
#             if target >= nums[split_idx]:
#                 return self.rec(nums, split_idx, r, target)
#             else:
#                 return self.rec(nums, l, split_idx - 1, target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(solution.search(nums, target))

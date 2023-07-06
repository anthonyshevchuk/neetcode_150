from typing import List


# solution set must not contain duplicate triplets


# bruteforce
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    sum_ = nums[i] + nums[j] + nums[k]
                    out = [nums[i], nums[j], nums[k]]
                    out.sort()
                    sorted_indices = tuple(out)
                    if sum_ == 0 and sorted_indices not in seen:
                        res.append(out)
                        seen.add(sorted_indices)
        return res


# optimal solution with sorting and reducing to 2sum II
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            # two sum II starts here
            while l < r:
                sum_ = v + nums[l] + nums[r]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    # upd only left
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_case = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(test_case))

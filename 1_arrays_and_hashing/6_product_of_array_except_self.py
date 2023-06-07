# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefixes, postfixes = [], []
        for i in range(len(nums)):
            num = nums[i]
            if len(prefixes) == 0:
                prefixes.append(num)
            else:
                next = prefixes[-1] * num
                prefixes.append(next)

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if len(postfixes) == 0:
                postfixes.append(num)
            else:
                next = postfixes[0] * num
                postfixes.insert(0, next)

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfixes[i + 1])
            elif i == len(nums) - 1:
                output.append(prefixes[i - 1])
            else:
                output.append(prefixes[i - 1] * postfixes[i+1])

        return output


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 2, 3, 4]
    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums))
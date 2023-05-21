# https://leetcode.com/problems/contains-duplicate/

# len(set) и len(list) занимает O(1) времени, потому что под капотом на C++ есть counter при append/pop
# dict это hashtable, который всегда O(1) на поиск, вставку, удаление

# операция преобразования листа в сет занимает O(n) времени

# операция поиска в сете:
# операция поиска в листе:
# сравнение двух несортированных листов:


class Solution(object):
    def containsDuplicate(self, nums):  # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = {}  # this could be just a set
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

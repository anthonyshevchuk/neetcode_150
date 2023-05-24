# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for str in strs:
            freq = tuple(sorted(str))
            hashmap[freq].append(str)

        return [hashmap[k] for k in hashmap.keys()]


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))





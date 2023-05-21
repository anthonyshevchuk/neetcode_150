# https://leetcode.com/problems/valid-anagram/
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_freq = self.str2freq(s)
        t_freq = self.str2freq(t)

        if s_freq == t_freq:
            return True
        return False

    def str2freq(self, string):
        # freq = dict()
        # for char in string:
        #     if char not in freq:
        #         freq[char] = 0  # как-то раз на собесе меня поправили
        #     freq[char] += 1
        freq = defaultdict(int)
        for c in string:
            freq[c] += 1
        return freq


if __name__ == "__main__":
    solution = Solution()
    # s, t = "anagram", "nagaram"
    s, t = "aacc", "ccac"
    print(solution.isAnagram(s, t))

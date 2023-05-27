# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


# мое первое решение
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        # O(m x nlog(n) x 26) -> O(m x nlog(n), где m - кол-во строк, n - ср. длина строки, а 26 - кол-во англ. букв
        for str in strs:
            freq = tuple(sorted(str))  # сортирую буквы и преобразую в кортеж - hashable (чтоб юзать как key в dict)
            hashmap[freq].append(str)

        return [hashmap[k] for k in hashmap.keys()]


# оптимальное решение без сортировки, хотя судя по литкоду - с сортировкой работает быстрее... почему ? :)
class Solution1(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for str in strs:
            count_vector = [0 for i in range(26)]
            for char in str:
                idx = ord(char) - ord('a')  # эта ф-ция возвращает ASCI индекс, и мы нормализуем (чтоб первый == 0)
                count_vector[idx] += 1
            key = tuple(count_vector)  # превратим лист в tuple, так как он - hashable, и может быть key в dict
            hashmap[key].append(str)  # по памяти O(m x n)? Где n - ср. кол-во строк в группе?

        return hashmap.values()


if __name__ == "__main__":
    # solution = Solution()
    solution = Solution1()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))

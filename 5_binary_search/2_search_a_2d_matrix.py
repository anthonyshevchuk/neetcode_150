from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search a row in a matrix
        l, r = 0, len(matrix) - 1
        row = None
        while l <= r:
            m = l + ((r - l) // 2)
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = matrix[m]
                break

        if row:
            l, r = 0, len(row) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if target < row[m]:
                    r = m - 1
                elif target > row[m]:
                    l = m + 1
                else:
                    return True
        return False



if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # matrix = [[1]]
    # matrix = [[1], [3]]
    target = 1
    # target = 2
    # target = 1
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
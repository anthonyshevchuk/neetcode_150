# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict

# first solution
class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # validate rows
        for i in range(9):
            counts = defaultdict(int)
            for num in board[i]:
                if num != '.':
                    counts[num] += 1
                    if counts[num] > 1:
                        return False

        # validate cols
        for i in range(9):
            counts = defaultdict(int)
            for row in board:
                if row[i] != '.':
                    counts[row[i]] += 1
                    if counts[row[i]] > 1:
                        return False

        for block_row_start in range(0, 9, 3):
            for block_col_start in range(0, 9, 3):
                counts = defaultdict(int)
                for row_idx in range(block_row_start, block_row_start + 3):
                    for col_idx in range(block_col_start, block_col_start + 3):
                        value = board[row_idx][col_idx]
                        if value != '.':
                            counts[value] += 1
                            if counts[value] > 1:
                                return False

        return True


# second optimal (a little more btw)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # validate rows
        for i in range(9):
            counts = defaultdict(int)
            for num in board[i]:
                if num != '.':
                    counts[num] += 1
                    if counts[num] > 1:
                        return False

        # validate cols
        for i in range(9):
            counts = defaultdict(int)
            for row in board:
                if row[i] != '.':
                    counts[row[i]] += 1
                    if counts[row[i]] > 1:
                        return False

        hashmap = defaultdict(set)
        for row_idx in range(9):
            for col_idx in range(9):
                value = board[row_idx][col_idx]
                if value != '.':
                    box_id = (row_idx // 3, col_idx // 3)
                    if value not in hashmap[box_id]:
                        hashmap[box_id].add(value)
                    else:
                        return False

        return True






if __name__ == "__main__":
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    # board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(solution.isValidSudoku(board))

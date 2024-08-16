# https://leetcode.com/problems/valid-sudoku/description/
import collections


def solution(sudoku):
    row_dict = collections.defaultdict(set)
    col_dict = collections.defaultdict(set)
    square_dict = collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] != ".":
                if (sudoku[r][c] in row_dict[r] or
                        sudoku[r][c] in col_dict[c] or
                        sudoku[r][c] in square_dict[(r // 3, c // 3)]):
                    return False
                row_dict[r].add(sudoku[r][c])
                col_dict[c].add(sudoku[r][c])
                square_dict[(r // 3, c // 3)].add(sudoku[r][c])
    return True


# 37. Sudoku Solver
# Difficulty: Hard
# Write a program to solve a Sudoku puzzle by filling the empty cells.

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, num):
            # Check row
            if num in board[row]:
                return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if isValid(board, i, j, num):
                                board[i][j] = num
                                
                                if solve(board):
                                    return True
                                
                                board[i][j] = '.'
                        
                        return False
            
            return True
        
        solve(board)


# Test
if __name__ == "__main__":
    sol = Solution()
    
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    sol.solveSudoku(board)
    for row in board:
        print(row)

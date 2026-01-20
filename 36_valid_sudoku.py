# 36. Valid Sudoku
# Difficulty: Medium
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated.

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':
                    continue
                
                box_idx = (i // 3) * 3 + (j // 3)
                
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        
        return True


# Test
if __name__ == "__main__":
    sol = Solution()
    
    board1 = [
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
    print(sol.isValidSudoku(board1))  # True

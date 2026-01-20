# 48. Rotate Image
# Difficulty: Medium
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()


# Test
if __name__ == "__main__":
    sol = Solution()
    
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    print(matrix1)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix2)
    print(matrix2)

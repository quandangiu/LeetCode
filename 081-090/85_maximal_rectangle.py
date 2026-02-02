class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        max_area = 0
        heights = [0] * len(matrix[0])
        
        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = []
            temp_heights = heights + [0]
            
            for i, h in enumerate(temp_heights):
                while stack and temp_heights[stack[-1]] > h:
                    height = temp_heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        
        return max_area

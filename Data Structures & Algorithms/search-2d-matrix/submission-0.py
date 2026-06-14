class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left = 0
        right =  rows * cols -1
        middle = (right + left) // 2 
        while left < right:
            i, j = middle // cols, middle % cols 
            if target <= matrix[i][j]:
                right = middle
            else:
                left = middle +1
            middle = (right + left) // 2 
        i, j = middle // cols, middle % cols
        return matrix[i][j] == target
            

        
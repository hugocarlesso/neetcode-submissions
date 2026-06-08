class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # a 90 degree rotation = reverse vertically then transpose
        # reverse rows
        matrix.reverse()
        n = len(matrix)
        #transpose:
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
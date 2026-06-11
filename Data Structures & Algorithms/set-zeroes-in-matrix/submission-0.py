class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # brut force solution:
        m,n = len(matrix), len(matrix[0])
        index_to_zero_out = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    index_to_zero_out.append([i,j])
        
        for index in index_to_zero_out:
            i,j = index[0], index[1]
            for p in range(m):
                matrix[p][j] =0
            for q in range(n):
                matrix[i][q] =0

        
        
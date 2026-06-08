class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # defining the index of the wall
        right = len(matrix[0])-1
        left = 0
        top = 0
        bottom = len(matrix) -1

        while left <= right and top <= bottom:

            # following top wall
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            
            # following right wall
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            # Safety check for non-square matrices
            if not (left <= right and top <= bottom):
                break
            # following bottom wall
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -=1

            # following left wall
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left +=1
        return result

            





    

"""
order
(0,0) --> 0 = 
(0,1) --> 1 = 
(0,2) --> 2 = 
(1,2) --> 3 = 
(2,2) --> 4 = 
(2,1) --> 5 = 
(2,0) --> 6 =
"""
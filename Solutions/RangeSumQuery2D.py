from typing import List

# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.pf = matrix
#         for i in range(len(matrix)):
#             for j in range(1,len(matrix[0])):
#                 self.pf[i][j] = self.pf[i][j-1] + matrix[i][j]


#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         sum = 0
#         for i in range(row1, row2+1):
#             sum += self.pf[i][col2] - self.pf[i][col1-1]
#         return sum

# an error appears with an edge case:
# [[[[-1]]],[0,0,0,0]]
# the issue is that when col1 is zero our og code goes to a -1 which refers to the
# last element in the list in python
# to avoid this we add an extra column of all zeros
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pf = [[0]*(len(matrix[0])+1) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(1, (len(matrix[0])+1)): #add extra column for zeros j = 1 to 5
                self.pf[i][j] = self.pf[i][j-1] + matrix[i][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            sum += self.pf[i][col2+1] - self.pf[i][col1]
        return sum

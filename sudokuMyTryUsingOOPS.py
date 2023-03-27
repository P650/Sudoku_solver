class SudokuSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def isValid(self, x, y, val):
        for j in range(0, 9):
            if (self.matrix[x][j] == val):
                return False

        for i in range(0, 9):
            if (self.matrix[i][y] == val):
                return False

        submati = x - (x % 3)
        submatj = y - (y % 3)

        for i in range(0, 3):
            for j in range(0, 3):
                if(self.matrix[submati + i][submatj + j] == val):
                    return False

        return True
    
    def solve(self):
        return self.sudokuSolver(0, 0)
    
    def sudokuSolver(self, i, j):
        if j == 9:
            if i == 8:
                return True
            i += 1
            j = 0

        if self.matrix[i][j] > 0:
            return self.sudokuSolver(i, j+1)

        for val in range(1, 10):
            if self.isValid(i, j, val):
                self.matrix[i][j] = val
                if self.sudokuSolver(i, j+1):
                    return True

            self.matrix[i][j] = 0

        return False


# Example usage
matrix = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 8, 5, 0, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

solver = SudokuSolver(matrix)
solver.solve()
print(matrix)
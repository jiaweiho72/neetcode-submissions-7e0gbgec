class NumMatrix:
    """
    question
    - sumRegion must be O(1)
        - you can't iterate and sum every cell every call

    idea
    - precompute
        - cell value = sum of nodes from origin to cell
        sum = lower_right - (left side) - (top side) + (top left region)
        top left region because left and top will overlap
    - precompute is just for each row, for each col, add to the prefix sum on top along with the current row's sum

    """
    def _precompute(self, matrix, prefix_sum_matrix, rows, cols):
        print(matrix, prefix_sum_matrix, rows, cols)
        for r in range(rows):
            cur_row_sum = 0
            for c in range(cols):
                cell = matrix[r][c]
                cur_row_sum += cell
                prefix_sum_matrix[r][c] += cur_row_sum

                top = r - 1
                if top in range(rows):
                    prefix_sum_matrix[r][c] += prefix_sum_matrix[top][c]
        

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix_sum_matrix = [[0] * self.cols for _ in range(self.rows)]
        self._precompute(matrix, self.prefix_sum_matrix, self.rows, self.cols)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full_sum = left_sum = left_diagonal_sum = top_sum = 0

        # Full sum
        full_sum = self.prefix_sum_matrix[row2][col2]

        # left region
        if col1 - 1 in range(self.cols):
            left_sum = self.prefix_sum_matrix[row2][col1 - 1]
        # left_diagonal
        if col1 - 1 in range(self.cols) and row1 - 1 in range(self.rows):
            left_diagonal_sum = self.prefix_sum_matrix[row1 - 1][col1 - 1]
        # top region
        if row1 - 1 in range(self.rows):
            top_sum = self.prefix_sum_matrix[row1 - 1][col2]
        
        return full_sum - left_sum - top_sum + left_diagonal_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
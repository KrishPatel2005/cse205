class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            # Initialize sets to keep track of seen numbers in rows, columns, and sub-boxes.
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subbox_sets = [set() for _ in range(9)]
        
        # Iterate through each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                current_num = board[i][j]
                
                # Check if the current cell is filled
                if current_num != ".":
                    # Check if the current number is already seen in the current row, column, or sub-box
                    if current_num in row_sets[i] or current_num in col_sets[j] or current_num in subbox_sets[i//3 * 3 + j//3]:
                        return False  # Invalid Sudoku
                    else:
                        # Add the current number to the respective sets
                        row_sets[i].add(current_num)
                        col_sets[j].add(current_num)
                        subbox_sets[i//3 * 3 + j//3].add(current_num)
        
        return True  # Valid Sudoku
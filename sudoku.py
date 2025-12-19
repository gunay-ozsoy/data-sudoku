"""Sudoku validator module."""

REQUIRED = set(range(1, 10))


def sudoku_validator(grid):
    """Return True if given 9x9 grid is a valid Sudoku solution, else False."""
    if not _is_valid_shape(grid):
        return False

    if not _has_only_valid_numbers(grid):
        return False

    if not _rows_valid(grid):
        return False

    if not _cols_valid(grid):
        return False

    if not _boxes_valid(grid):
        return False

    return True


def _is_valid_shape(grid):
    """Check grid is a 9x9 list of lists."""
    if not isinstance(grid, list) or len(grid) != 9:
        return False
    return all(isinstance(row, list) and len(row) == 9 for row in grid)


def _has_only_valid_numbers(grid):
    """Check all cells are ints in REQUIRED."""
    for row in grid:
        for value in row:
            if not isinstance(value, int) or value not in REQUIRED:
                return False
    return True


def _rows_valid(grid):
    """Check each row contains exactly numbers 1..9."""
    return all(set(row) == REQUIRED for row in grid)


def _cols_valid(grid):
    """Check each column contains exactly numbers 1..9."""
    for col_idx in range(9):
        column = {grid[row_idx][col_idx] for row_idx in range(9)}
        if column != REQUIRED:
            return False
    return True


def _boxes_valid(grid):
    """Check each 3x3 sub-box contains exactly numbers 1..9."""
    for box_row in (0, 3, 6):
        for box_col in (0, 3, 6):
            box = {
                grid[row_idx][col_idx]
                for row_idx in range(box_row, box_row + 3)
                for col_idx in range(box_col, box_col + 3)
            }
            if box != REQUIRED:
                return False
    return True

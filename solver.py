
class SudokuSolver:
    WHITE = (255, 255, 255)

    def solve(self, grid, surface, x, y):

        while grid.default_grid[y][x] != 0 or grid.editable_grid[y][x] != 0:
            if x < 8:
                x += 1
            elif x == 8 and y < 8:
                x = 0
                y += 1
            elif x == 8 and y == 8:  # the base case
                return True
        for value in range(1, 10):
            if grid.check_valid_position(x, y, value):
                grid.editable_grid[y][x] = value

                if self.solve(grid, surface, x, y):
                    return True

                # if there is no possible value, reset the cell value.
                grid.editable_grid[y][x] = 0

        return False

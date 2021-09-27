import pygame
import random as r
from player import PlayerInteractions
pygame.init()


class GridHandler:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIGHT_BLUE = (102, 204, 255)
    LIGHT_GRAY = (179, 179, 179)

    FONT_S = pygame.font.SysFont("ubuntumono", 20)
    FONT_L = pygame.font.SysFont("ubuntumono", 30)

    sqr_len = 60
    empty_cells = 81
    player = PlayerInteractions()

    blocks_dict = {1: [0, 0, 2, 2], 2: [3, 0, 5, 2], 3: [6, 0, 8, 2],
                   4: [0, 3, 2, 5], 5: [3, 3, 5, 5], 6: [6, 3, 8, 5],
                   7: [0, 6, 2, 8], 8: [3, 6, 5, 8], 9: [6, 6, 8, 8]}

    default_grid, editable_grid = [], []

    def __init__(self):
        self.default_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.editable_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    """
    - Returns True if the position and value of the random number/ user input are valid.
    - Displays a hint "invalid input, The value exists at the same block/row/column".
    """
    def check_valid_position(self, x, y, value):
        x_min, y_min, x_max, y_max = 0, 0, 0, 0

        # Determining what block i'm standing at
        for i in range(1, 10):
            x_min, y_min, x_max, y_max = self.blocks_dict[i]
            if x >= x_min and y >= y_min:
                if x <= x_max and y <= y_max:
                    block = i
                    break

        # Check if the value exists in the same block.
        for i in range(y_min, y_max+1):
            for j in range(x_min, x_max+1):
                if self.default_grid[i][j] == value or self.editable_grid[i][j] == value:
                    return False

        # Check if the value exists in the same row.
        for i in range(9):
            if self.default_grid[y][i] == value or self.editable_grid[y][i] == value:
                return False

        # Check if the value exists in the same column.
        for i in range(9):
            if self.default_grid[i][x] == value or self.editable_grid[i][x] == value:
                return False
        return True

    """
    - Returns the initial grid with random numbers in random positions in every block.
    """
    def set_default_grid(self):

        for block in range(1, 10):
            n_positions = r.randint(1, 4)  # number of values that will be generated in the block.

            for pos in range(n_positions):
                x_min, y_min, x_max, y_max = self.blocks_dict[block]
                x = r.randint(x_min, x_max)
                y = r.randint(y_min, y_max)
                value = r.randint(1, 9)

                if self.default_grid[y][x] == 0:
                    if self.check_valid_position(x, y, value):
                        self.default_grid[y][x] = value
                        self.empty_cells = self.empty_cells-1

    """
    - Draws the grid with the updated values.
    - Paints the current cell with blue color.
    """
    def update_grid(self, surface, current_x, current_y):

        self.player.display_instructions(surface)
        self.player.solve_button(surface)
        self.player.clear_button(surface)
        self.player.new_game_button(surface)

        sur_x, sur_y = 30, 30  # position of x and y on the surface.

        for i in range(9):
            for j in range(9):

                # If this cell is the current cell the player pointing at, paint it with blue.
                if i == current_y and j == current_x:
                    pygame.draw.rect(surface, self.LIGHT_BLUE, pygame.Rect(sur_x, sur_y, self.sqr_len, self.sqr_len))

                    if self.default_grid[i][j] != 0:
                        # The player can't change this value so it's going to be framed with red.
                        pygame.draw.rect(surface, self.RED, pygame.Rect(sur_x, sur_y, self.sqr_len, self.sqr_len), 2)
                        text = self.FONT_L.render(str(self.default_grid[i][j]), True, self.BLACK)
                        surface.blit(text, (sur_x + 20, sur_y + 15))

                # Paint the default cell with gray.
                elif self.default_grid[i][j] != 0:
                    pygame.draw.rect(surface, self.LIGHT_GRAY, pygame.Rect(sur_x, sur_y, self.sqr_len, self.sqr_len))
                    pygame.draw.rect(surface, self.BLACK, pygame.Rect(sur_x, sur_y, self.sqr_len, self.sqr_len), 2)

                    # Printing the numbers
                    text = self.FONT_L.render(str(self.default_grid[i][j]), True, self.BLACK)
                    surface.blit(text, (sur_x + 20, sur_y + 15))

                # If the cell is empty, paint it with white.
                else:
                    pygame.draw.rect(surface, self.BLACK, pygame.Rect(sur_x, sur_y, self.sqr_len, self.sqr_len), 2)

                if self.editable_grid[i][j] != 0:
                    text = self.FONT_L.render(str(self.editable_grid[i][j]), True, self.BLACK)
                    surface.blit(text, (sur_x + 20, sur_y + 15))

                    # Drawing the borders of each block.
                if i % 3 == 0 and j % 3 == 0:
                    pygame.draw.rect(surface, self.BLACK, pygame.Rect(sur_x, sur_y, self.sqr_len * 3, self.sqr_len * 3), 8)

                sur_x += 60
            sur_x, sur_y = 30, sur_y + 60

    """
    - Update the grid with the user input if the entered value is valid.
    """
    def update_grid_values(self, surface, x, y, value):

        if self.default_grid[y][x] == 0:

            # Empty the cell if the user clicked on the spacebar.
            if value == -1:
                self.editable_grid[y][x] = 0
                self.empty_cells += 1  # increase the number of empty cells.
                return False

            if self.check_valid_position(x, y, value):
                self.editable_grid[y][x] = value
                self.empty_cells -= 1
                if self.empty_cells == 0:
                    return True
            elif value != 0:  # invalid input.
                self.player.display_invalid_input(surface, 1)
        elif value != 0:
            self.player.display_invalid_input(surface, 2)

    """
    - Returns the grid to its primal state. 
    """
    def clear_grid(self, surface):
        for i in range(9):
            for j in range(9):
                if self.editable_grid[j][i] != 0:
                    self.editable_grid[j][i] = 0
                    self.empty_cells += 1
        surface.fill(self.WHITE)
        self.update_grid(surface, 4, 4)


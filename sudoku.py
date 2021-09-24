import pygame
from grid import GridHandler
from solver import SudokuSolver
from player import PlayerInteractions


# Defining Colors & Variables
pygame.init()
WHITE = (255, 255, 255)

SURFACE_HEIGHT = 730
SURFACE_WIDTH = 730
SURFACE_SIZE = (SURFACE_WIDTH, SURFACE_HEIGHT)

# Establishing the SURFACE & THE DEFAULT GRID
surface = pygame.display.set_mode(SURFACE_SIZE)
pygame.display.set_caption("Sudoku")
surface.fill(WHITE)

grid = GridHandler()
grid.set_default_grid()

player = PlayerInteractions()

# Setting the initial position for the player in the middle of the grid to move from.
current_x, current_y = 4, 4
grid.update_grid(surface, current_x, current_y)

# The main program loop.
game_on = True
clock = pygame.time.Clock()

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if the player clicks close.
            game_on = False

        elif event.type == pygame.KEYDOWN:  # if the player hits the keyboard.
            surface.fill(WHITE)
            current_x, current_y, value = player.movement(event, current_x, current_y)
            finished = grid.update_grid_values(surface, current_x, current_y, value)
            grid.update_grid(surface, current_x, current_y)
            if finished:  # if the player finished the sudoku puzzle.
                player.display_congrats(surface)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # if the player clicks on the buttons.
            click = pygame.mouse.get_pos()

            if 600 <= click[0] <= 710 and 390 <= click[1] <= 450:  # if the player clicked on the Solve button.
                solver = SudokuSolver()
                if solver.solve(grid, surface, 0, 0):
                    grid.update_grid(surface, current_x, current_y)
                    player.display_endgame(surface, 1)

                else:
                    player.display_endgame(surface, 0)

            elif 600 <= click[0] <= 710 and 510 <= click[1] <= 570:  # if the player clicked on the Clear button.
                grid.clear_grid(surface)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

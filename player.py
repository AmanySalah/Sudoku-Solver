import pygame
pygame.init()


class PlayerInteractions:

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    LIGHT_GRAY = (179, 179, 179)

    FONT_L = pygame.font.SysFont("ubuntumono", 30)
    FONT_S = pygame.font.SysFont("ubuntumono", 20)

    keys_set = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3,
                pygame.K_KP4, pygame.K_KP5, pygame.K_KP6,
                pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

    def movement(self, event, x, y):

        number = 0
        if event.key == pygame.K_LEFT:
            if x > 0:
                x -= 1
        if event.key == pygame.K_RIGHT:
            if x < 8:
                x += 1
        if event.key == pygame.K_UP:
            if y > 0:
                y -= 1
        if event.key == pygame.K_DOWN:
            if y < 8:
                y += 1
        #  If the player enters a number from the numeric keypad.
        if event.key in self.keys_set:
            number = int(event.unicode)
        # Empty the cell if it's filled.
        if event.key == pygame.K_SPACE:
            number = -1

        return x, y, number

    def display_invalid_input(self, surface, choice):
        sur_x, sur_y = 30, 580
        invalid_input = ["- Invalid input, the value exists at the same block/ row/ column.",
                         "- You can't change this value."]
        if choice == 1:
            text = self.FONT_S.render(invalid_input[0], True, self.RED)
            surface.blit(text, (sur_x, sur_y))
        elif choice == 2:
            text = self.FONT_S.render(invalid_input[1], True, self.RED)
            surface.blit(text, (sur_x, sur_y))

    def display_instructions(self, surface):
        sur_x, sur_y = 30, 600
        instructions = ["- Use the keyboard arrows to move among the cells.",
                        "- Press the spacebar ro clear the cell.",
                        "- Enter a number form you numeric keypad."]
        for inst in instructions:
            text = self.FONT_S.render(inst, True, self.BLACK)
            surface.blit(text, (sur_x, sur_y))
            sur_y += 20

    def solve_button(self, surface):
        sur_x, sur_y = 600, 390

        pygame.draw.rect(surface, self.LIGHT_GRAY, pygame.Rect(sur_x, sur_y, 110, 60))
        text = self.FONT_L.render("Solve", True, self.BLACK)
        surface.blit(text, (sur_x+15, sur_y+15))

    def clear_button(self, surface):
        sur_x, sur_y = 600, 510
        pygame.draw.rect(surface, self.LIGHT_GRAY, pygame.Rect(sur_x, sur_y, 110, 60))
        text = self.FONT_L.render("Clear", True, self.BLACK)
        surface.blit(text, (sur_x+15, sur_y+15))

    def display_endgame(self, surface, choice):
        congrats = "Congratulations!!"
        deadend = "Dead End!"
        sur_x, sur_y = 210, 680
        if choice == 1:
            text = self.FONT_L.render(congrats, True, self.RED)
            surface.blit(text, (sur_x, sur_y))
        else:
            text = self.FONT_L.render(deadend, True, self.RED)
            surface.blit(text, (sur_x, sur_y))

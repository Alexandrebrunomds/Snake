import sys
import game_over
from control.constantes import *
from game_over import *
import time
from random import *
import pygame


# Sound effects links
# Apple: https://freesound.org/people/AlienXXX/sounds/132504/
# Game over: https://freesound.org/people/ScreamStudio/sounds/412168/


# Lists to store the coordinates of the snake's body parts
pygame.init()
x_snake_position = [0]
y_snake_position = [0]
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")
cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((144, 238, 144))
window.blit(cover, (0, 0))


# Refreshing the screen to display everything
pygame.display.flip()


# Loading the main images on the game window
head_up = pygame.image.load("assets/arthur_santos_head_snake_up.png").convert_alpha()  # The head
head_up = pygame.transform.scale(head_up, (30, 30))
head_left = pygame.image.load("assets/arthur_santos_head_snake_left.png").convert_alpha()
head_left = pygame.transform.scale(head_left, (30, 30))
head_down = pygame.image.load("assets/arthur_santos_head_snake_down.png").convert_alpha()
head_down = pygame.transform.scale(head_down, (30, 30))
head_right = pygame.image.load("assets/arthur_santos_head_snake_right.png").convert_alpha()
head_right = pygame.transform.scale(head_right, (30, 30))
body_part_1 = pygame.image.load("assets/arthur_santos_body.png").convert_alpha()  # The body
body_part_1 = pygame.transform.scale(body_part_1, (30, 30))
fruit = pygame.image.load("assets/arthur_santos_apple.png").convert_alpha()  # The fruit
fruit = pygame.transform.scale(fruit, (30, 30))
wall = pygame.image.load("assets/arthur_santos_wall.png").convert_alpha()
wall = pygame.transform.scale(wall, (25, 50))


# Storing the head and fruit's coordinates in variables
position_1 = head_down.get_rect()
position_fruit = fruit.get_rect()

# Storing the variables in the list variables created before
x_snake_position[0] = 250
y_snake_position[0] = 250


# Giving random coordinates to the first fruit of the game
position_fruit.x = randint(2, 10) * STEP
position_fruit.y = randint(2, 10) * STEP


for i in range(0, 1000):
    x_snake_position.append(-100)
    y_snake_position.append(-100)


def collision(x_coordinates_1, y_coordinates_1, x_coordinates_2, y_coordinates_2, size_snake, size_fruit):
    if ((x_coordinates_1 + size_snake >= x_coordinates_2) or (x_coordinates_1 >= x_coordinates_2))\
            and x_coordinates_1 <= x_coordinates_2 + size_fruit:
        if ((y_coordinates_1 >= y_coordinates_2) or (
                y_coordinates_1 + size_snake >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
            return True
        return False


def text_score(score_temp):
    font = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 25)
    text = font.render("Score: " + str(score_temp), True, (0, 0, 0))
    window.blit(text, (500, 0))


# Create Walls
def walls():
    for i in range(34):
        wall_x = pygame.transform.rotate(wall, 180)
        window.blit(wall, (-3+(i*18), 5))
        window.blit(wall_x, (-3+(i*18), 564))
    for j in range(31):
        wall_y = pygame.transform.rotate(wall, 90)
        wall_y_2 = pygame.transform.rotate(wall_y, 180)
        window.blit(wall_y, (-13, 27 + (j * 18)))
        window.blit(wall_y_2, (564, 27 + (j * 18)))


def main():
    playing = True
    score_temp = 0
    snake = SNAKE
    move_up = MOVE_UP
    move_down = MOVE_DOWN
    move_right = MOVE_RiGHT
    move_left = MOVE_LEFT
    move_init = MOVE_INIT

    # Sound effect
    apple_sound = pygame.mixer.Sound('assets/Apple-crunch.wav')
    apple_sound.set_volume(0.1)
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if move_up is False and move_init is True:
                        if move_down is True:
                            move_up = False
                        else:
                            move_down = move_right = move_left = False
                            move_up = move_init = True
                if event.key == pygame.K_DOWN:
                    if move_down is False:
                        if move_up is True:
                            move_down = False
                        else:
                            move_right = move_left = move_up = False
                            move_down = move_init = True
                if event.key == pygame.K_RIGHT:
                    if move_right is False:
                        if move_left is True:
                            move_right = False
                        else:
                            move_left = move_up = move_down = False
                            move_right = move_init = True
                if event.key == pygame.K_LEFT:
                    if move_left is False:
                        if move_right is True:
                            move_left = False
                        else:
                            move_right = move_down = move_up = False
                            move_left = move_init = True

        window.fill((144, 238, 144))
        window.blit(head_down, (250, 250))

        # Moving each part of the body by giving them new coordinates
        for i in range(snake - 1, 0, -1):
            x_snake_position[i] = x_snake_position[(i - 1)]
            y_snake_position[i] = y_snake_position[(i - 1)]

        # Filling the window with white to erase the different parts of the snake
        cover.fill((144, 238, 144))

        for i in range(1, snake):
            cover.blit(body_part_1, (x_snake_position[i], y_snake_position[i]))

        # Moving the snake in a certain direction if the user presses a key
        if move_up:
            y_snake_position[0] = y_snake_position[0] - STEP
            window.blit(cover, (0, 0))
            window.blit(head_up, (x_snake_position[0], y_snake_position[0]))

        if move_down:
            y_snake_position[0] = y_snake_position[0] + STEP
            window.blit(cover, (0, 0))
            window.blit(head_down, (x_snake_position[0], y_snake_position[0]))

        if move_right:
            x_snake_position[0] = x_snake_position[0] + STEP
            window.blit(cover, (0, 0))
            window.blit(head_right, (x_snake_position[0], y_snake_position[0]))

        if move_left:
            x_snake_position[0] = x_snake_position[0] - STEP
            window.blit(cover, (0, 0))
            window.blit(head_left, (x_snake_position[0], y_snake_position[0]))

        # Calling the collision function to check if the snake hits the edges of the window
        if x_snake_position[0] < window_rect.left:
            x_snake_position[0] = 250
            y_snake_position[0] = 250
            game_over(score_temp)
            set_click()

        if x_snake_position[0] + 35 > window_rect.right:
            x_snake_position[0] = 250
            y_snake_position[0] = 250
            game_over(score_temp)
            set_click()

        if y_snake_position[0] <= window_rect.top:
            x_snake_position[0] = 250
            y_snake_position[0] = 250
            game_over(score_temp)
            set_click()

        if y_snake_position[0] + 35 >= window_rect.bottom:
            x_snake_position[0] = 250
            y_snake_position[0] = 250
            game_over(score_temp)
            set_click()

        if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i], y_snake_position[i], 0, 0)\
                and MOVE_INIT:
            x_snake_position[0] = 250
            y_snake_position[0] = 250
            game_over(score_temp)
            set_click()
        window.blit(fruit, position_fruit)

        if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y, 20, 15):

            position_fruit.x = randint(1, 20) * STEP
            position_fruit.y = randint(1, 20) * STEP

            for j in range(0, snake):

                while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j], 20,
                                15):
                    position_fruit.x = randint(1, 20) * STEP
                    position_fruit.y = randint(1, 20) * STEP

            # Increasing the size of the snake and the score
            snake = snake + 1
            score_temp = score_temp + 1
            apple_sound.play()
        # Displaying the score
        walls()
        text_score(score_temp)
        pygame.display.flip()
        # Delaying the game to make the snake move fluent
        time.sleep(SPEED / 1000)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

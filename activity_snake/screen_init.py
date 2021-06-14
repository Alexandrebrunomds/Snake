import sys
import time
import pygame

import menu
import snake
import credits
pygame.init()
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")
image = pygame.image.load("assets/arthur_santos_init-screen.png").convert_alpha()
image = pygame.transform.scale(image, (600, 600))


def main():
    window.blit(image, (0, 0))
    pygame.display.update()
    time.sleep(3)
    menu.menu()


if __name__ == '__main__':
    main()

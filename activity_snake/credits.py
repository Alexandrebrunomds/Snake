import sys
import time
import pygame
import snake
import menu

pygame.init()
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")
image = pygame.image.load("assets/arthur_santos_credits-screen.png").convert_alpha()
image = pygame.transform.scale(image, (600, 600))
click = False


def main():
    click = False
    while not click:
        window.blit(image, (0, 0))
        font_2 = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 24)
        text_2 = "Press space to back menu"
        text_back = font_2.render(text_2, True, (0, 0, 0))
        text_back_rect = text_back.get_rect()
        text_back_rect.center = (300, 520)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.menu()
                    click = True

        window.blit(text_back, text_back_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()

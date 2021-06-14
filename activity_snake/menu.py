import sys
import time
import pygame
import snake
import credits
pygame.init()
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")
image = pygame.image.load("assets/arthur_santos_menu-screen.png").convert_alpha()
image = pygame.transform.scale(image, (600, 600))
click = False


def menu():
    click = False
    while not click:
        window.blit(image, (0, 0))
        font_2 = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 58)
        text_1 = 'PLAY'
        text_2 = "CREDITS"
        text_3 = 'EXIT'
        text_1 = font_2.render(text_1, True, (0, 0, 0))
        text_2 = font_2.render(text_2, True, (0, 0, 0))
        text_3 = font_2.render(text_3, True, (0, 0, 0))
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_1_rect.center = (300, 170)
        text_2_rect.center = (300, 300)
        text_3_rect.center = (300, 430)
        pos_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_1_rect.collidepoint(pos_mouse):
                    snake.main()
                    click = True
                if text_2_rect.collidepoint(pos_mouse):
                    credits.main()
                    click = True
                    pygame.display.update()

                if text_3_rect.collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()

            window.blit(text_1, text_1_rect)
            window.blit(text_2, text_2_rect)
            window.blit(text_3, text_3_rect)
            pygame.display.update()


if __name__ == '__main__':
    menu()

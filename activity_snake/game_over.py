import sys
import time
import pygame
import snake
import menu

pygame.init()
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")
score = 0

click = False


def game_over(score):
    global click
    flag = 0
    while not click:
        window.fill((144, 238, 144))
        font = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 48)
        font_2 = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 38)
        text_1 = 'GAME OVER'
        text_2 = "Press space to back menu"
        text_3 = 'Score:' + str(score)
        text_1 = font.render(text_1, True, (0, 0, 0))
        text_2 = font_2.render(text_2, True, (0, 0, 0))
        text_3 = font_2.render(text_3, True, (0, 0, 0))
        text_1_rect = text_1.get_rect()
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_1_rect.center = (300, 250)
        text_2_rect.center = (300, 350)
        text_3_rect.center = (300, 450)
        if flag == 0:
            death_sound = pygame.mixer.Sound('assets/')
            death_sound.set_volume(0.1)
            death_sound.play()
            flag = 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.menu()
                    click = True
        window.blit(text_1, text_1_rect)
        window.blit(text_2, text_2_rect)
        window.blit(text_3, text_3_rect)
        pygame.display.update()


def set_click():
    global click
    click = False


if __name__ == '__main__':
    game_over(score)


import pygame
import sys
from assets.car import Car
from assets.track import Track

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ali Racing Car")

clock = pygame.time.Clock()
car = Car()
track = Track()

font = pygame.font.SysFont(None, 55)
win_text = font.render("Congratulations Ali!", True, (255, 255, 0))

win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    car.update(keys)

    screen.fill((135, 206, 235))  # sky blue background
    track.draw(screen)
    car.draw(screen)

    if car.rect.x > 700:
        win = True

    if win:
        screen.blit(win_text, (250, 100))

    pygame.display.flip()
    clock.tick(60)

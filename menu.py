import pygame
import random
import math
from pygame import mixer

pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("start.png")

def run_game():
    import game

running = True
while running:

    #Screen Colour
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_ESCAPE:
                run_game()
            running = False
    pygame.display.update()

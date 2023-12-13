import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Fenêtre test")
screen.fill("White")
image_chaton = pygame.image.load("Image_chaton.jpg")
image_chaton = pygame.transform.scale(image_chaton, (200,150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_chaton, (400, 250))
    pygame.display.update()
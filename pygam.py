import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
running = True

while running:
    screen.fill((255, 255, 255))  # White background

    pygame.draw.rect(screen, (255, 0, 0), (200, 150, 150, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

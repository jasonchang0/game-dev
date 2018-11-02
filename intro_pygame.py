import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption('Display Sample Image')
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # Updating the current display at 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()








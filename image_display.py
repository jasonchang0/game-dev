import pygame

pygame.init()

display_width = 863
display_height = 576

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Display Sample Image')
clock = pygame.time.Clock()

img = pygame.image.load('sample.jpg')

def dislpay_img(toBeDisplayed, x, y):
    '''
    Blit -> 'BL'ock 'I'mage 'T'ranfser

    Screen is simply a collection of pixels,
    and blitting is doing a complete copy of
    one set of pixels onto another.

    :param x:
    :param y:
    :return:
    '''
    gameDisplay.blit(toBeDisplayed, (x, y))

crashed = False

while not crashed:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        elif event.type == pygame.QUIT:
            crashed = True

        # print(event)

    dislpay_img(img, 0, 0)

    # Updating the current display at 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
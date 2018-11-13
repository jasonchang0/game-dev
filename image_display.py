import pygame
import time
import random

pygame.init()

display_width = 1232
display_height = 816

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Display Sample Image')
clock = pygame.time.Clock()

img = pygame.image.load('sample_reduce.jpg')
img = pygame.transform.scale(img, (display_width // 4, display_height // 4))
img = pygame.transform.rotate(img, 90)

img_width = display_height // 4
img_height = display_width // 4


def draw_blocks(obj_x, obj_y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [obj_x, obj_y, width, height])


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


def text_objects(text, font):
    text_surf = font.render(text, True, black)
    return text_surf, text_surf.get_rect()


def message_display(text):
    text_style = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, text_style)
    text_rect.center = ((display_width/2), (display_height/2))

    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()

    time.sleep(10)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = display_width * 0.45
    y = display_height * 0.60

    dx = 0

    block_speed = 10
    block_width = 40
    block_height = 40
    block_start_y = -750
    block_start_x = random.randrange(0, display_width - block_width)


    exit_game = False

    while not exit_game:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # exit_game = True
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -10

                elif event.key == pygame.K_RIGHT:
                    dx = 10

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0

            # print(event)

        x += dx

        # Changing background color
        gameDisplay.fill(white)

        draw_blocks(block_start_x, block_start_y, block_width, block_height, black)
        block_start_y += block_speed

        dislpay_img(img, x, y)

        if not 0 < x < display_width - img_width:
            crash()

        if block_start_y > display_height:
            block_start_y = - block_height
            block_start_x = random.randrange(0, display_width - block_width)

        # Updating the current display at 60fps
        pygame.display.update()
        clock.tick(60)


game_loop()

pygame.quit()
quit()









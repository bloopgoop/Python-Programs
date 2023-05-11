import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()
snail_surface = pygame.image.load('snail1.png').convert_alpha()

sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()

snail_x_position = 600


#Gets image from sprite sheet, blits it to a surface of width and height,
#scales it and makes the color colour transparent.
def get_image(sheet, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0,0), (504, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image

frame_0 = get_image(sprite_sheet_image, 24, 24, 4)

while True:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    #display image
    screen.blit(frame_0, (0,0))

    snail_x_position -= 4
    if snail_x_position < -100:
        snail_x_position = 800
    screen.blit(snail_surface, (snail_x_position,280))

    pygame.display.update()
    clock.tick(60)
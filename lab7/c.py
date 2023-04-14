import pygame
pygame.init()

WIDTH, HEIGHT = 850, 450
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

finished = False

cir_x, cir_y = WIDTH // 2, HEIGHT // 2
RAD = 25
step = 20

while not finished:
    clock.tick(FPS)

    screen.fill(BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keydowns = pygame.key.get_pressed()

    if keydowns[pygame.K_UP] and cir_y - RAD > 0:
        cir_y -= step
    if keydowns[pygame.K_DOWN] and cir_y + RAD < HEIGHT:
        cir_y += step
    if keydowns[pygame.K_LEFT] and cir_x - RAD > 0:
        cir_x -= step
    if keydowns[pygame.K_RIGHT] and cir_x + RAD < WIDTH:
        cir_x += step
    
    pygame.draw.circle(screen, RED, (cir_x, cir_y), RAD)

    pygame.display.flip()
pygame.quit()
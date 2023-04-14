import pygame 
from datetime import datetime
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 1

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MICKEY CLOCK")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

background = pygame.image.load('./img/backg.jpg')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))  #настраиваем картинку по параметрам

hand1 = pygame.image.load('./img/ruka1.png').convert_alpha()     #преобразовывает поверхности в тот же формат 
hand2 = pygame.image.load('./img/ruka2.png').convert_alpha()     # пикселей, который используется на экране

pygame.mixer.music.load("music/tikanie.mp3")
pygame.mixer.music.play(-1)

def blitRotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = pos).center)
    surf.blit(rotated_image, new_rect.topleft)

finished = False

def time_to_angle(time):
    return time * 6

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.blit(background, (0, 0))
    
    t = datetime.now()
    text_time = font.render(f'{t:%H:%M:%S}', True, WHITE, BLACK)
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    screen.blit(text_time,(50, 75))

    angle_sec = time_to_angle(t.second + 1)
    angle_min = time_to_angle(t.minute)

    blitRotate(screen, hand1, (250, 150), -angle_sec)
    blitRotate(screen, hand2, (250, 150), -angle_min)

    pygame.display.flip()
pygame.quit()
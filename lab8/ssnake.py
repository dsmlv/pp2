import pygame
from random import randrange
pygame.init()

WIDTH, HEIGHT = 400, 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font_big = pygame.font.SysFont("Arial", 20)
font_small = pygame.font.SysFont("Arial", 10)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

#Loading the Sound
sound = pygame.mixer.Sound('music/biting.wav')

#Creating the text for winning
winning = font_small.render(f'YOU WON! CONGRATULATIONS', True, BLACK)

#Snake's global variables
RAD = 10
block = 20

def position():
    x = randrange(0, WIDTH - 50, block)
    y = randrange(0, HEIGHT - 50, block)
    return x, y

food_rad = 6
food_x, food_y = position()


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, PINK, (self.x, self.y, 20, 20))
    
restart = True
while restart:
    FPS = 6

    finished = False
    lose = False
    win = False

    #Snake's variables
    body = [[100, 100], [0, 0], [0, 0]]
    dx, dy = block, 0
    direction = ''

    score = 0
    cnt = 0
    level = 1

    while not finished:
        clock.tick(FPS)

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                restart = False

            #restart by tapping the space   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                finished = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and direction != 'left':
                    dx = block
                    dy = 0
                    direction = 'right'
                if event.key == pygame.K_LEFT and direction != 'right':
                    dx = -block
                    dy = 0
                    direction = 'left'
                if event.key == pygame.K_UP and direction != 'down':
                    dx = 0
                    dy = -block
                    direction = 'up'
                if event.key == pygame.K_DOWN and direction != 'up':
                    dx = 0
                    dy = block
                    direction = 'down'

        #Reading the txt files of walls
        walls_coor = open(f'levels/level{level}.txt', 'r').readlines()
        walls = []
        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Wall(j * 20, i * 20))

        #Movement of the snake
        for i in range(len(body) - 1, 0, -1):
            body[i][0] = body[i - 1][0]
            body[i][1] = body[i - 1][1]
    
        #Change snake's head position
        body[0][0] += dx
        body[0][1] += dy
    
        #Movement outside the playing area
        if body[0][0] > WIDTH:
            body[0][0] = 0
        if body[0][0] < 0:
            body[0][0] = WIDTH
        if body[0][1] > HEIGHT - 50:
            body[0][1] = 0
        if body[0][1] < 0:
            body[0][1] = HEIGHT - 50

        #Collision with food:
        if body[0][0] == food_x and body[0][1] == food_y:
            sound.play()
            body.append([800, 800])
            score += 1
            cnt += 1
            food_x, food_y = position()

        #Collision with snake:
        if body[0] in body[1:]:
            lose = True

        #Drawing the walls
        for wall in walls:
            wall.draw()

            #Checking and redrawing the food
            if wall.x == food_x and wall.y == food_y:
                food_x, food_y = position()
                pygame.draw.circle(screen, BLUE, (food_x, food_y), food_rad)

            #Collision with walls:
            if wall.x + block == body[0][0] and wall.y == body[0][1] :
                lose = True

        #Level up
        if cnt == 5:
            level += 1
            FPS += 1
            cnt = 0

        #Winning condition
        if level == 5:
            win = True

        #Draw the food
        pygame.draw.circle(screen, BLUE, (food_x, food_y), food_rad)

        #Draw snake
        for i, (x, y) in enumerate(body):
            if i == 0:
                color = RED 
            else: color = GREEN

            pygame.draw.circle(screen, color, (x, y), RAD)

        #Texts
        losing = font_small.render(f'GAME OVER! YOU LOST WITH {score}', True, BLACK)
        tapping = font_small.render(f'TAP SPACE TO RESTART', True, BLACK)

        while lose or win:
            pygame.draw.rect(screen, WHITE, (100, 100, 200, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False

                #restart by tapping the space   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    lose = False
                    win = False
                    finished = True

            if lose:
                screen.blit(losing, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 30))

            if win:
                screen.blit(winning, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 30))

            pygame.display.flip()

        #Texts
        score_text = font_big.render(f'SCORE: {score}', True, WHITE)
        level_text = font_big.render(f'LEVEL: {level}', True, WHITE)
        screen.blit(score_text, (20, 410))
        screen.blit(level_text, (300, 410))

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()   

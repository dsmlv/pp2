import pygame
from random import randrange, choice
pygame.init()

#Global variables
WIDTH, HEIGHT = 400, 450
cell = 20
score_pos = (20, 410)
level_pos = (325, 410)

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

#Creating the Clock
clock = pygame.time.Clock()

#Creating the font for texts
font_big = pygame.font.SysFont("Arial", 20)
font = pygame.font.SysFont("Arial", 10)

#Loading the images
level_up = pygame.image.load('img/snake/level-up.png')
cupcake = pygame.transform.scale(pygame.image.load('img/snake/cupcake.png'), (30, 30))
food1 = pygame.transform.scale(pygame.image.load(f'img/snake/food1.png'), (30, 30))
food2 = pygame.transform.scale(pygame.image.load(f'img/snake/food2.png'), (30, 30))
food3 = pygame.transform.scale(pygame.image.load(f'img/snake/food3.png'), (30, 30))
food4 = pygame.transform.scale(pygame.image.load(f'img/snake/food4.png'), (30, 30))

#The list of the food
food_list = [food1, food2, food3, food4]

#Loading the Sound
sound = pygame.mixer.Sound('music/biting.wav')

#Creating the text for winning
winning = font.render(f'YOU WON! CONGRATULATIONS', True, BLACK)

#Creating the Userevent for the superfood
NEXT = pygame.USEREVENT 
pygame.time.set_timer(NEXT, 5000)

class Superfood:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT - 50, cell)

    def draw(self):
        superfood_rect = pygame.Rect(self.x, self.y, cell, cell)
        screen.blit(cupcake, superfood_rect)
        
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT - 50, cell)

class Food:
    def __init__(self, img):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT - 50, cell)
        self.img = img

    def draw(self):
        food_rect = pygame.Rect(self.x, self.y, cell, cell)
        screen.blit(self.img, food_rect)
       
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT - 50, cell)
        self.img = choice(food_list)

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))

class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN
    
    def move(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'

        #Movement of the snake
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        #Change snake's head position
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        #Movement outside the playing area
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT - 50

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    
    #Collision with food
    def collide_food(self, f: Food):
        global SCORE
        global cnt
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.body.append([1000, 1000])
            sound.play()
            cnt += 1
            if f.img == food1:
                SCORE += 1
            elif f.img == food2:
                SCORE += 1
            elif f.img == food3:
                SCORE += 0.5
            elif f.img == food4:
                SCORE += 2

    def collide_superfood(self, sf: Superfood):
        global SCORE
        global cnt
        if self.body[0][0] == sf.x and self.body[0][1] == sf.y:
            self.body.append([1000, 1000])
            sound.play()
            cnt += 1
            SCORE += 5
        
        
    #Collision with snake       
    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:
            lose = True

    #Checking the place of food appearance
    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()

restart = True

while restart:
    FPS = 7

    finished = False
    lose = False
    win = False

    food = Food(choice(food_list))  
    snake = Snake()
    superfood = Superfood()

    level = 1
    SCORE = 0
    cnt = 0   #for level up
    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)

        screen.blit(level_up, (345, 410)) 

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
                restart = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                finished = True
            if event.type == NEXT:
                superfood.redraw() #teleporting the superfood after the 5 sec

        #Reading the txt files of walls
        walls_coor = open(f'levels/level{level}.txt', 'r').readlines()
        walls = []
        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Wall(j * cell, i * cell))

        #Drawing and moving the objects
        food.draw()
        superfood.draw()
        snake.draw()
        snake.move()
        
        #Snake's collision
        snake.collide_food(food)
        snake.collide_superfood(superfood)
        snake.collide_self()
        snake.check_food(food)
        snake.check_food(superfood)

        #Drawing the walls
        for wall in walls:
            wall.draw()

            #Checking the food appearance
            if food.x == wall.x and food.y == wall.y:
                food.redraw()
            
            if superfood.x == wall.x and superfood.y == wall.y:
                superfood.redraw()

            #Collision with walls
            if snake.body[0][0] == wall.x and snake.body[0][1] == wall.y:
                lose = True

        #Increasing the speed and level up
        if cnt == 5:
            FPS += 2 
            level += 1
            cnt = 0
        
        #Winning condition
        if level == 5:
            win = True

        #Texts
        losing = font.render(f'GAME OVER! YOU LOST WITH {SCORE} p', True, BLACK)
        on_level = font.render(f'at the level {level}', True, BLACK)
        tapping = font.render(f'TAP SPACE TO RESTART', True, BLACK)

        while lose or win:
            pygame.draw.rect(screen, WHITE, (100, 100, 200, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    lose = False
                    win = False
                    finished = True

            if lose:
                screen.blit(losing, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(on_level, (WIDTH // 2 - 34 , HEIGHT // 2 - 30))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 5))

            if win:
                screen.blit(winning, (WIDTH // 2 - 84 , HEIGHT // 2 - 50))
                screen.blit(tapping, (WIDTH // 2 - 74 , HEIGHT // 2 - 30))

            pygame.display.flip()
        
        #Texts
        score_text = font_big.render(f'SCORE: {SCORE}', True, RED)
        level_text = font_big.render(f'{level}', True, PURPLE)
        screen.blit(score_text, (score_pos[0], score_pos[1]))
        screen.blit(level_text, (level_pos[0], level_pos[1]))
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
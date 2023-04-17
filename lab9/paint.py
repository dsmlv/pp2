import pygame
from random import randint
from math import *
pygame.init()

#Global variables
WIDTH, HEIGHT = 800, 600
FPS = 60
RAD = 30

#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Creating the Clock
clock = pygame.time.Clock()

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def getDist(start_pos, end_pos):
    return sqrt((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2)

#Drawing a rectangle
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

#Drawing a сircle
def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

#Drawing a right triangle
def drawTriangle(color, pos):
    pygame.draw.polygon(screen, color, pos, 4)

#Drawing an equilateral triangle
def drawEqTrianle(color, pos):
    pygame.draw.polygon(screen, color, pos, 4)

#Drawing a rhombus
def drawRhom(color, pos):
    pygame.draw.polygon(screen, color, pos, 4)

#Drawing a square
def drawSquare(color, pos):
    pygame.draw.polygon(screen, color, pos, 4)

#Drawing a circle as an eraser
def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

#Variables
finished = False
drawing = False
color = BLACK

screen.fill(WHITE)

#Creating the font for text
font_big = pygame.font.SysFont("Times New Roman", 14)
text = font_big.render(f'1 - Rectangle; 2 - Circle; 3 - Eraser; 4 - Right triangle; 5 - Equilateral triangle; 6 - Rhombus; 7 - Square', True, BLACK)

#Loading the images
palitra = pygame.transform.scale(pygame.image.load('img/paint/palitra.png'), (100, 100))

#Position of our drawing objects
start_pos = 0
end_pos = 0

#For drawing the figures
mode = 0
    # 0 - Rect
    # 1 - Circle
    # 2 - Eraser
    # 3 - Right triangle
    # 4 - Equilateral triangle
    # 5 - Rhombus
    # 6 - Square

while not finished:
    clock.tick(FPS)

    #Creating a variable, which saves the coordinates of mouse
    pos = pygame.mouse.get_pos()

    #Showing the image
    screen.blit(palitra, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        #Clicking by mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos #saving position to the start_pos

            #Choosing the color
            if pos[0] > 0 and pos[0] < palitra.get_width() and pos[1] > 0 and pos[1] < palitra.get_height():
                color = screen.get_at(pos)

        #Releasing the mouse
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos #saving position to the end_pos

            rect_x = abs(start_pos[0] - end_pos[0]) #for calculatng the width pf the rectangle
            rect_y = abs(start_pos[1] - end_pos[1]) #for calculatng the height pf the rectangle
            
            #Rectangle
            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)

            #Circle
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)

            #Right triangle
            elif mode == 3:
                drawTriangle(color, [start_pos, end_pos, (start_pos[0], end_pos[1])])

            #Equilateral triangle
            elif mode == 4:

                #Coordinates of the 3rd side
                x3 = (end_pos[0] - start_pos[0]) * cos(pi/3) - (end_pos[1] - start_pos[1]) * sin(pi/3) + start_pos[0]
                y3 = (end_pos[0] - start_pos[0]) * sin(pi/3) + (end_pos[1] - start_pos[1]) * cos(pi/3) + start_pos[1]

                drawEqTrianle(color, [start_pos, end_pos, (x3, y3)])

            #Rhombus
            elif mode == 5:
                d = getDist(start_pos, end_pos) #Distance between two points
                drawRhom(color, [start_pos, (start_pos[0] + d, start_pos[1]), (end_pos[0] + d, end_pos[1]), end_pos])
            
            #Square
            elif mode == 6:
                d = getDist(start_pos, end_pos) #Distance between two points
                x2 = (start_pos[0] + d, start_pos[1])
                x3 = (x2[0], x2[1] + d)
                drawSquare(color, [start_pos,  x2, x3, (start_pos[0], start_pos[1] + d)])

        
        if event.type == pygame.MOUSEMOTION and drawing: #moving the mouse to erase 
            if mode == 2:
                eraser(pos, RAD)
        
        #Choosing the mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 0
            if event.key == pygame.K_2:
                mode = 1
            if event.key == pygame.K_3:
                mode = 2
            if event.key == pygame.K_4:
                mode = 3
            if event.key == pygame.K_5:
                mode = 4
            if event.key == pygame.K_6:
                mode = 5
            if event.key == pygame.K_7:
                mode = 6

            #Deleting all objects
            if event.key == pygame.K_BACKSPACE:
                screen.fill(WHITE)           
    #Text
    screen.blit(text, (150, 10))
    pygame.display.flip()
pygame.quit()
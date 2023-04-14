import pygame
pygame.init()

#Global variables
WIDTH, HEIGHT = 800, 600
FPS = 60
RAD = 30

#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAINT')

#Creating the Clock
clock = pygame.time.Clock()

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Drawing a rectangle
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

#Drawing a circle
def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

#Drawing a circle as an eraser
def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

#Variables
finished = False
drawing = False
color = BLACK

screen.fill(WHITE)

#Creating the font for text
font_big = pygame.font.SysFont("Arial", 20)
text = font_big.render(f'1 - Rectangle; 2 - Circle; 3 - Eraser', True, BLACK)

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

            rect_x = abs(start_pos[0] - end_pos[0]) #for calculatng the width of the rectangle
            rect_y = abs(start_pos[1] - end_pos[1]) #for calculatng the height of the rectangle
            
            #Rectangle
            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)

            #Circle
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
            
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

            #Deleting all objects
            if event.key == pygame.K_BACKSPACE:
                screen.fill(pygame.Color('white'))
    #Text
    screen.blit(text, (450, 10))
    pygame.display.flip()
pygame.quit()
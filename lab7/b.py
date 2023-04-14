import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Music player")      #выводит название игры в окне

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock =  pygame.time.Clock()

finished = False

songs = ['music/50 Cent - In da club.mp3', 'music/Beyonce (ft. Shakira) - Beatiful Liar.mp3', 'music/Britney Spears - Toxic.mp3', 'music/BTS - Ugh.mp3', 'music/Minelli - Rampampam.mp3']
pygame.mixer.music.load('music/50 Cent - In da club.mp3')
pygame.mixer.music.play()

font = pygame.font.SysFont('Verdana', 30)

img = pygame.image.load("./img/player.jpeg")        #загружает картинку и сохраняет его, далее изменение размера картинки
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]]                  #двигает песню в конец очереди
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
    

def play_prev_song():
    global songs
    songs =  [songs[-1]] + songs[:-1]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()


while not finished:
    clock.tick(FPS)             #игра работает не более 20 кадров в секунду

    screen.blit(img, (0,0))
    for event in pygame.event.get():                #получает события из следующей очереди
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_s:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                play_next_song()
            if event.key == pygame.K_LEFT:
                play_prev_song()
    
    name = songs[0].replace('music/', '')           
    song_name = name.replace('.mp3', '')            

    text = font.render(f'{song_name}', True, BLACK, WHITE)      #вставляем название песен
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 + 58))     #расположение текста

    pygame.display.flip() 
pygame.quit()
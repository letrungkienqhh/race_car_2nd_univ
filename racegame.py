#19630204 LE TRUNG KIEN
#中間課題
import pygame
import random
import time
pygame.init()


display_width = 1000
display_height = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('2D車-EASYGAME')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

carImg = pygame.image.load('carr.png')
cardown = pygame.image.load('carrdown.png')
def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(count), True, black)
    gameDisplay.blit(text,(5,5))
 
def car(x,y,cartype):
    gameDisplay.blit(cartype, (x,y))

def thing(x,y,w,h,color):
    pygame.draw.rect(gameDisplay,color,[x,y,w,h])




car_width=200
car_height=70
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    gameloop()
def crash(tensuu):
    
    pygame.mixer.music.load('crash.mp3')
    pygame.mixer.music.play(-1)
    if tensuu<10:
        text='....！！SCORE： '+str(tensuu)
    elif tensuu<20:
        text='Good！SCORE： '+str(tensuu)
    else:
        text='Excellent！SCORE： '+str(tensuu)
    message_display(text)
  

def gameloop():    
    x = (display_width * 0.1)
    y = (display_height * 0.7)
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    
    crashed = False
    y_change=0
    x_change=0
    thing_startx = display_width
    thing_starty = random.randrange(0, display_height)
    thing_speed =7
    thing_width = 100
    thing_height = 100
    scores=0
    iro=(0,0,0)
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #########################
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=+5
                elif event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=+5
            if event.type==pygame.KEYUP:
                y_change=0
                x_change=0
                
        thing_startx -=thing_speed
        y+=y_change
        x+=x_change
        if thing_startx <0-thing_width:
                thing_startx = display_width 
                thing_starty = random.randrange(0,display_height)
                thing_width=random.randrange(100,150)
                thing_height=thing_width
                scores+=1;
                if scores%3==0:
                    thing_speed+=2
                R = random.randrange(0, 257, 10)
                B = random.randrange(0, 257, 10)
                G = random.randrange(0, 257, 10)
                iro=(R,B,G)
        gameDisplay.fill(white)
        
        thing(thing_startx,thing_starty,thing_width,thing_width,iro)
        if x>thing_startx+thing_width:
            True  
        elif x+car_width>thing_startx:
            if (y+car_height>thing_starty and y+car_height<thing_starty+thing_height) or (y>thing_starty and y<thing_starty+thing_height):
                car(x-50,y,cardown)
                crash(scores)

        car(x,y,carImg)
        score(scores)
        ##
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
#game_introduce()
gameloop()
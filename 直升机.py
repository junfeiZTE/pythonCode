import pygame
import time
from random import randint

black=(0,0,0)
white=(255,255,255)

surfaceWidth=1000
surfaceHeight=600
imageHeight=110
imageWidth=107


pygame.init()
surface=pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock=pygame.time.Clock()

def blocks(x_block,y_block,block_width,block_height,gap,color):
    
    pygame.draw.rect(surface,color,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface,color,[x_block,y_block+block_height+gap,block_width,surfaceHeight-(y_block+block_height+gap)])

def helicopter(x,y,image):
    surface.blit(image,(x,y))

img=pygame.image.load('D:\\feiji.png')

##def replay_or_quit():
##    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP]):
##        if event.type == pygame.KEYDOWN:
##            return event.key
##
##        if event.type == pygame.UP:
##            return event.key
##    return None

def makeTextObjs(text,font):
    textSurface=font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def msgSurface(text):
    smallText=pygame.font.Font('D:\\freesansbold.ttf',20)
    largeText=pygame.font.Font('D:\\freesansbold.ttf',150)

    titleTextSurf,titleTextRect=makeTextObjs(text,largeText)
    titleTextRect.center=surfaceWidth/2,surfaceHeight/2
    surface.blit(titleTextSurf,titleTextRect)

    typTextSurf,typTextRect=makeTextObjs('Press any key to continue',smallText)
    typTextRect.center=surfaceWidth/2,surfaceHeight/2+100
    surface.blit(typTextSurf,typTextRect)
    
    pygame.display.update()
    time.sleep(3)

##    while replay_or_quit() == None:
##        clock.tick()
##
    pygame.quit()
def gameOver():
    msgSurface("Kaboom")

def main():
    x=150
    y=200

    x_block=surfaceWidth
    y_block=0
    block_width=75
    block_height=randint(0,surfaceHeight/2)
    gap=imageHeight*2
    
    color=(randint(0,255),randint(0,255),randint(0,255))
    cross_num=0
    block_move=(cross_num+1)*2

    y_move=0
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move=-5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move=5
        y+=y_move     
        surface.fill(black)
        helicopter(x,y,img)
        
        blocks(x_block,y_block,block_width,block_height,gap,color)
        x_block-=block_move
        
        if y<0 or y>surfaceHeight-100:
            print("Crash!!")
            gameOver()

        if x_block < (-1*block_width):
            x_block=surfaceWidth
            block_height=randint(0,surfaceHeight/2)
            color=(randint(0,255),randint(0,255),randint(0,255))
            if cross_num != 10:
                cross_num+=1
                block_move=(cross_num+1)*2

        if (x+imageWidth > x_block) and (x < x_block + block_width):
            if y < block_height or y+imageHeight > block_height+gap:
                print("Oh")
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()


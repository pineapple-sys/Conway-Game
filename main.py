#Print the result of game.py
import pygame, sys
from src import game
from src.config import *

def main():  
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT+PAUSE_PLAY_WINDOW))
    running = True
    timer = 0
    n, ones = game.start()
    # //PLAY/PAUSE BUTTON
    image = pygame.image.load("tf.webp").convert_alpha()
    image = pygame.transform.smoothscale(image, (PLAY_BUTTON_SIZE, PLAY_BUTTON_SIZE))
    image_rect = image.get_rect()
    image_rect.topleft = (WIDTH//2-PLAY_BUTTON_SIZE//2, HEIGHT+PAUSE_PLAY_WINDOW//4)
    #//
    play = True
    while running:
        dt = clock.tick(FPS)/1000
        timer +=dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                if image_rect.collidepoint(event.pos):
                    print('Pause/Play')
                    play = not(play)
                if not play:
                    if 0<=event.pos[0]<= WIDTH and 0 <= event.pos[1]<= HEIGHT:
                        coord = (round(event.pos[1]//CELLS_SIZE),round(event.pos[0]//CELLS_SIZE))
                        if coord not in ones:
                            ones.add(coord)
                        else:
                            ones.remove(coord)

        if timer >= COOLDOWN:
            timer = 0
            if play:
                ones = game.game(ones,GRID_SIZE)
                print(n)
        screen.fill(BACKGROUND_COLOR)
        screen.blit(image, (WIDTH//2-PLAY_BUTTON_SIZE//2, HEIGHT+PAUSE_PLAY_WINDOW//4))
        if ones:
            for i in ones:
                pygame.draw.rect(screen,CELL_COLOR,(i[1]*CELLS_SIZE,i[0]*CELLS_SIZE,CELLS_SIZE,CELLS_SIZE))   
        #--grille 
        for i in range(0,WIDTH+1,CELLS_SIZE):
            for j in range(0,HEIGHT+1,CELLS_SIZE):
                pygame.draw.rect(screen,GRID_COLOR,(0,0,i,j),1)
        #--
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


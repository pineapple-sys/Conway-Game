#Print the result of game.py
import pygame, sys
from src import game
from src.config import *

def main():  
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    timer = 0
    n, ones = game.start()
    while running:
        dt = clock.tick(FPS)/1000
        timer +=dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        if timer >= COOLDOWN:
            timer = 0
            n, ones= game.game(n)
            print(n)
        screen.fill(BACKGROUND_COLOR)
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


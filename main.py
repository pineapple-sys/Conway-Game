import pygame, game, sys,numpy as np

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 400,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ones = []

running = True
timer = 0
n = np.zeros((10,10),dtype ="int64")
#Place un glider comme exemple
n[2][3] = 1
n[1][2] = 1
ones.append([2,3])
ones.append([1,2])
for i in range(1,4):
    n[3][i]= 1
    ones.append([3,i])


while running:
    dt = clock.tick(60)/1000
    timer +=dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    
    if timer >= 1:
        timer = 0
        n = game.game(n)
        print(n)
        ones = []
        for i in range(len(n)):
            for j in range(len(n)):
                if n[i][j] == 1:
                    ones.append([i,j])
    screen.fill((0,0,0))
    if ones:
        for i in ones:
            pygame.draw.rect(screen,(255,255,255),(i[1]*40,i[0]*40,40,40))
            
    #--grille 
    for i in range(0,WIDTH+1,40):
        for j in range(0,HEIGHT+1,40):
            pygame.draw.rect(screen,(128,128,128),(0,0,i,j),1)
    #--
    
    pygame.display.flip()
pygame.quit()
sys.exit()

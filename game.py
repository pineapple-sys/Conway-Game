import numpy as np
import math

def dist(x,y):
    a = [x[0]-y[0],x[1]-y[1]]
    return int(math.sqrt(a[0]**2 + a[1]**2))

def game(n):
    grid = n
    new = np.zeros((10,10),dtype ="int64")
    
    #répertorie la pos de chaque 1 de la matrice dans la liste "ones"
    ones = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                ones.append([i,j])

    #Regarde la distance entre chaque carré et un 1 présent sur une case diff de lui meme, compte le nombre de fois ou cette condition est remplie et remplace le numéro de la case par ce nombre de fois
    for i in range(len(grid)):
        for j in range(len(grid)):
            count = 0
            for o in ones:
                if [i,j]!=o:
                    if dist([i,j],o) ==1:
                        count+=1
            if  grid[i][j] !=1:
                grid[i][j] = count
            else:
                grid[i][j] = count

    #inscrit les 1 dans la matrice "new" en fonction des règles du jeu
    for i in range(len(grid)):
        for j in range(len(grid)):
            if [i,j] not in ones:
                if grid[i][j] == 3:
                    new[i][j] = 1
            else:
                if 2<=grid[i][j]<=3:
                    new[i][j] = 1
    grid = new
    return new
















"""
[i-1,j-1]  [i-1,j]  [i-1,j+1]
[i,j-1]     [i,j]    [i,j+1]
[i+1,j-1]  [i+1,j]  [i+1,j+1]
"""



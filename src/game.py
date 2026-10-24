#This is where the game play itself

import numpy as np
import sys

sys.path.append('../Conway_Game/src')
from config import *

def start(): 
    ones = set()
    n = np.zeros((GRID_SIZE,GRID_SIZE),dtype ="int64")
    #Place un glider comme exemple
    n[2][3] = 1
    n[1][2] = 1
    ones.add((2,3))
    ones.add((1,2))
    for i in range(1,4):
        n[3][i]= 1
        ones.add((3,i))
    return n, ones

def game(n):
    grid = n
    new = np.zeros((GRID_SIZE,GRID_SIZE),dtype ="int64")
    
    #répertorie la pos de chaque 1 de la matrice dans la liste "ref"
    
    ref = set(tuple(cell) for cell in np.argwhere(grid == 1))

    ones = set()
    #Regarde la distance entre chaque carré et un 1 présent sur une case diff de lui meme, compte le nombre de fois ou cette condition est remplie et remplace le numéro de la case par ce nombre de fois
    for i in range(len(grid)):
        for j in range(len(grid)):
            count = 0
            for o in ref:
                if (i,j)!=o:
                    if abs(o[0]-i) <=1 and abs(o[1]-j)<=1:
                        count+=1
            
            #inscrit les 1 dans la matrice "new" en fonction des règles du jeu 
            #Ajoute aussi les 1 dans la nouvelle matrice renvoyée a main..
            #..cette matrice sera ensuite envoyée au prochain tour par main, et new sera donc grid
            if (((i,j) not in ref) and count == 3) or ((i,j) in ref  and (2 <= count <= 3)):
                # Une cellule MORTE avec exactement 3 voisins NAÎT
                new[i][j] = 1  
                ones.add((i,j)) 
            
    print(ones)
    return new, ones


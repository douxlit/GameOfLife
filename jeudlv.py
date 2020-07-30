import matplotlib.pyplot as plt
import numpy as np
from time import time
from random import random

init_time = time() #temps auquel on veut que le jeu commence (en utilisant time) -> int

##Modification git

#modif test
#modif test 2 from GitHub

##regle jeu de la vie

#Une cellule ne survie au tour suivant que si elle est entourée par 2 ou 3 cellules "vivantes"

#Une cellule vide entourée d'exactement 3 cellules "vivantes" devient elle même vivante au tour suivant

##fonction sur tableau numpy

essaie = np.ones((5,5))
e1 = np.array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
       
e2 = np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])

def countones(tab,l,c) :
    k = 0
    (n,p) = tab.shape
    if tab[l,c] == 1 :
        k-=1
    if l != 0 and l != n-1 and c != 0 and c != p-1 :
        for i in range (l-1,l+2) :
            for j in range (c-1,c+2) :
                if tab[i,j] == 1 :
                    k+=1
        return k
        
    
    end

def tab2jdlv(tab) :
    (n,p) = tab.shape
    intermediaire = tab.tolist()
    for i in range (1,n-1) :
        for j in range (1,p-1) :
            if tab[i,j] == 0 and countones(tab,i,j) == 3 :
                intermediaire[i][j] = 1
            if tab[i,j] == 1 :
                if countones(tab,i,j) < 2 or countones(tab,i,j) > 3 :
                    intermediaire[i][j] = 0
    
    return np.array(intermediaire)
    
    end
random
##fonction du 'temps'1595867650

def jdlv_time(tab,temps):
    if temps == 0 :
        return tab
    else :
        return jdlv_time(tab2jdlv(tab), temps-1) #vive la recursivité
        
##agrandissement du tableau 

def extend(tab,more_l,more_c) :
    (n,p) = tab.shape
    E = np.zeros((n+2*more_l,p+2*more_c))
    for i in range (n) :
        for j in range (p) :
            E[i+more_l,j+more_c] = tab[i,j]
    return E

##agrandissement + fonction du temps (bof pas la meilleure solution)

def jdlv_tex(tab,temps,extension) :
    if temps == 0 :
        return tab
    else :
        return jdlv_tex(  tab2jdlv(  extend(tab,extension,extension)  ), temps-1, extension ) #vive la recursivité
        
##test1

# t = time()
# T = int(t) - init_time
# print(jdlv_tex(e,T,0)) #permet d'avoir un jdlv qui evolue toutes les secondes et qui grandit toutes les secondes

##definition "nature" 

def prob(k,p) :
    """proba p qu'une cellule k change d'état"""
    assert (k==0 or k==1) and 0<=p<=1
    x = random()
    if x > p :
        return k
    else :
        return abs(k-1)

#cond de cht d'etat d'une cellule ?

#si rien aux alentours d'une cellule vide (>=N) p = x
#si cellule vivante aux alentours d'une cellule vide (<N) p = 10x 

def cellule_autour(N,i,j,tab) :
    
    (n,p)=tab.shape
    
    if i-N < 0 :
        for l in range (0,i+N+1) :
            
            if j-N < 0 :
                for c in range (0,j+N+1) :
                    if tab[l,c] == 1 :
                        return True
            elif j+N+1 > p :
                for c in range (j-N,p) :
                    if tab[l,c] == 1 :
                        return True
            else :
                for c in range (j-N,j+N+1) :
                    if tab[l,c] == 1 :
                        return True

    elif i+N+1 > n :
        for l in range (i-N,n) :
            
            if j-N < 0 :
                for c in range (0,j+N+1) :
                        if tab[l,c] == 1 :
                            return True
            elif j+N+1 > p :
                for c in range (j-N,p) :
                        if tab[l,c] == 1 :
                            return True
            else :
                for c in range (j-N,j+N+1) :
                    if tab[l,c] == 1 :
                        return True
    
    elif j-N < 0 :
        for c in range (0,j+N+1) :
            if i-N < 0 :
                for l in range (0,i+N+1) :
                    if tab[l,c] == 1 :
                        return True
            elif i+N+1 > n :
                for l in range (i-N,p) :
                    if tab[l,c] == 1 :
                        return True
            else :
                for l in range (i-N,i+N+1) :
                    if tab[l,c] == 1 :
                        return True
                        
    elif j+N+1 > p :
        for c in range (j-N,p) :
            
            if i-N < 0 :
                for l in range (0,i+N+1) :
                    if tab[l,c] == 1 :
                        return True
            elif i+N+1 > n :
                for l in range (i-N,n) :
                    if tab[l,c] == 1 :
                        return True    
            else :
                for l in range (i-N,i+N+1) :
                    if tab[l,c] == 1 :
                        return True         
                        
    else :
        for l in range (i-N,i+N+1) :
            for c in range (j-N,j+N+1) :
                if tab[l,c] == 1 :
                    return True
                    
    return False








    





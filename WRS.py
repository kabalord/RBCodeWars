#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:32:59 2020

@author: walterroaserrano
"""
import numpy as np
t = [[1,9,1],[2,9,1],[2,1,1]]
start = (0,0)
finish = (0,2)

def cheapest_path(t,start,finish):
    
    reponse = np.zeros_like(t)
    reponse[start] = 1
    x_current = start[0]
    y_current = start[1]
    cout = t
    
    while x_current != finish[0] or y_current != finish[1]:
        
        posible_mov = [-1,1,-1,1]        
        cout_meilleur_voisin = 99999
        coordonneeX = 0
        coordonneeY = 0
        
        
        for i in range(4):
            
            if i < 2:
                x_voisin = x_current + posible_mov[i]
                y_voisin = y_current
                print(x_voisin)
            if i >= 2:
                x_voisin = x_current
                y_voisin = y_current + posible_mov[i]
                print(y_voisin)
            if (x_voisin >= 0 and y_voisin >= 0) and (reponse[(x_voisin, y_voisin)] != 1):
                print()
                if cout[x_voisin][y_voisin] < cout_meilleur_voisin:
                    cout_meilleur_voisin = cout[x_voisin][y_voisin]
                    coordonneeX = x_voisin
                    coordonneeY = y_voisin
            
        x_current = coordonneeX
        y_current = coordonneeY
        reponse[x_current][y_current] = 1
    print(reponse)
    print(x_current,y_current)
    
        
                
    

cheapest_path(t,start,finish)   
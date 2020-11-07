#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:32:59 2020

@author: walterroaserrano
"""
import numpy as np
t = np.array([[1,9,1],[2,9,1],[2,1,1]])
start_row = 0
start_col = 0
finish_row = 0
finish_col = 2

def cheapest_path(t,start_row,start_col,finish_row,finish_col):
    
    reponse = np.zeros_like(t)
    reponse[start_row][start_col] = 1
    current_col = start_col
    current_row = start_row
    cout = t
    cout_rows = cout.shape[0]
    cout_cols = cout.shape[1]
    
    while current_row != finish_row or current_col != finish_col:
        
        posible_mov = [-1,1,-1,1]        
        cout_meilleur_voisin = 99999
        coordonnee_col = 0
        coordonnee_row = 0
        
        
        for i in range(4):
            
            if i >= 2:
                voisin_col = current_col
                voisin_row = current_row + posible_mov[i]
                print(voisin_row)
            
            if i < 2:
                voisin_col = current_col + posible_mov[i]
                voisin_row = current_row
                print(voisin_col)

            if (voisin_col >= 0 and voisin_row >= 0 and voisin_col < cout_cols and voisin_row < cout_rows) and (reponse[voisin_row][voisin_col] != 1):
                print()                
                if cout[voisin_row][voisin_col] < cout_meilleur_voisin:
                    cout_meilleur_voisin = cout[voisin_row][voisin_col]
                    coordonnee_row = voisin_row
                    coordonnee_col = voisin_col
                    
            
        current_row = coordonnee_row
        current_col = coordonnee_col        
        reponse[current_row][current_col] = 1
    print("reponse : ")
    print(reponse)

    
        
                
    

cheapest_path(t,start_row,start_col,finish_row,finish_col)   
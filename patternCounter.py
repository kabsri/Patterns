#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 00:46:41 2018

@author: kabilan
"""

#Adjacency matrix for which grid points can go to which other grid points
#I used an empty row and column for the 0th node because it's easier for me to think in terms of 1-9
M = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,1,0,1,1,1,0,1,0],
     [0,1,0,1,1,1,1,1,0,1],
     [0,0,1,0,1,1,1,0,1,0],
     [0,1,1,1,0,1,0,1,1,1],
     [0,1,1,1,1,0,1,1,1,1],
     [0,1,1,1,0,1,0,1,1,1],
     [0,0,1,0,1,1,1,0,1,0],
     [0,1,0,1,1,1,1,1,0,1],
     [0,0,1,0,1,1,1,0,1,0]]

def validPattern(pattern):
    used = []
    used.append(pattern[0])
    for p in range(0, len(pattern)-1):
        if M[pattern[p]][pattern[p+1]]==0 or pattern[p+1] in used:
            return False
        used.append(pattern[p+1])
    return True
        
sequences = [[1,3,4,5,3], [4,5,3,6,2,9,6], [3,4,6,4,5,7,4,7], [3,2,1,5,4,3,8]]

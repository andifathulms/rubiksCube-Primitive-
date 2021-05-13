# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:19:30 2020

@author: LENOVO
"""

class Side():
    face = [[" " for i in range(0,3)],
            [" " for i in range(0,3)],
            [" " for i in range(0,3)]]
    def __init__(self,color):
        self.face = [[color for i in range(0,3)],
                     [color for i in range(0,3)],
                     [color for i in range(0,3)]]
        
    def __getitem__(self,pos):
        i,j = pos
        return self.face[i][j]
    
    def __setitem__(self,pos,value):
        i,j = pos
        self.face[i][j] = value
    
    def printSide(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.face[i][j], end="  ")
            print()
    
    def isComplete(self):
        for i in range(0,3):
            for j in range(0,2):
                if self.face[i][j] != self.face[i][j+1]:
                    return False
        
        return True
#end class Side()
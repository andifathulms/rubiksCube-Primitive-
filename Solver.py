# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:56:49 2021

@author: LENOVO
"""

import Cube as cb

def adjustWhite(cube):
    if(cube.piecesPos("X2") == "W"):
          cube.doX()
    elif(cube.piecesPos("X1") == "W"):
        cube.doX().doX()
    elif(cube.piecesPos("X4") == "W"):
        cube.doX().doX().doX()

def solveWhiteEdge(cube):
    p1 = cube.piecesPos("E1")
    p2 = cube.piecesPos("E2")
    p3 = cube.piecesPos("E3")
    p4 = cube.piecesPos("E4")
    p5 = cube.piecesPos("E5")
    p6 = cube.piecesPos("E6")
    p7 = cube.piecesPos("E9")
    p8 = cube.piecesPos("E10")
    
    # Solve WG edge
    # Identified WG edge
    for i in [p1,p2,p3,p4,p5,p6,p7,p8] :
        if (i[0] == "W" and i[1] == "G") :
            piece = i 
            break
        if (i[0] == "G" and i[1] == "W") :
            pieceR = i 
            break
       
    

def solveBase(cube):
    
    adjustWhite(cube)
    solveWhiteEdge(cube)
    
    

def solveSecondLayer():
    return

def solveLastLayer():
    return

def solveCube(cube):
    
    solveBase()
    solveSecondLayer()
    solveLastLayer()
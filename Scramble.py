# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:21:15 2020

@author: LENOVO
"""

import math
import random as rand

class Scramble():
    def __init__(self,scramble):
        self.scr_li = list(scramble.split(" "))
    
    def __getitem__(self,key):
        return self.scr_li[key]
    
    def getLength(self):
        return len(self.scr_li)
    
    def showScramble(self):
        print(self.scr_li)

def runScramble(cube,scramble):
    s = scramble
    for i in range(0,s.getLength()):
        if s[i] in ["R","R2","R'","r","r2","r'"]:
            if s[i] in ["R","R2","R'"]:
                if s[i] == "R":
                    cube.doR()
                elif s[i] == "R'":
                    cube.doRp()
                elif s[i] == "R2":
                    cube.doR2()
            elif s[i] in ["r","r2","r'"]:
                if s[i] == "r":
                    cube.do_r()
                elif s[i] == "r'":
                    cube.do_rp()
                elif s[i] == "r2":
                    cube.do_r2()
        #end R rotation
        elif s[i] in ["L","L2","L'","l","l2","l'"]:
            if s[i] in ["L","L2","L'"]:
                if s[i] == "L":
                    cube.doL()
                elif s[i] == "L'":
                    cube.doLp()
                elif s[i] == "L2":
                    cube.doL2()
            elif s[i] in ["l","l2","l'"]:
                if s[i] == "l":
                    cube.do_l()
                elif s[i] == "l'":
                    cube.do_lp()
                elif s[i] == "l2":
                    cube.do_l2()
        #end L rotation
        elif s[i] in ["F","F2","F'","f","f2","f'"]:
            if s[i] in ["F","F2","F'"]:
                if s[i] == "F":
                    cube.doF()
                elif s[i] == "F'":
                    cube.doFp()
                elif s[i] == "F2":
                    cube.doF2()
            elif s[i] in ["f","f2","f'"]:
                if s[i] == "f":
                    cube.do_f()
                elif s[i] == "f'":
                    cube.do_fp()
                elif s[i] == "f2":
                    cube.do_f2()
        #end F rotation
        elif s[i] in ["B","B2","B'","b","b2","b'"]:
            if s[i] in ["B","B2","B'"]:
                if s[i] == "B":
                    cube.doB()
                elif s[i] == "B'":
                    cube.doBp()
                elif s[i] == "B2":
                    cube.doB2()
            elif s[i] in ["b","b2","b'"]:
                if s[i] == "b":
                    cube.do_b()
                elif s[i] == "b'":
                    cube.do_bp()
                elif s[i] == "b2":
                    cube.do_b2()
        #end B rotation
        elif s[i] in ["U","U2","U'","u","u2","u'"]:
            if s[i] in ["U","U2","U'"]:
                if s[i] == "U":
                    cube.doU()
                elif s[i] == "U'":
                    cube.doUp()
                elif s[i] == "U2":
                    cube.doU2()
            elif s[i] in ["u","u2","u'"]:
                if s[i] == "u":
                    cube.do_u()
                elif s[i] == "u'":
                    cube.do_up()
                elif s[i] == "u2":
                    cube.do_u2()
        #end U rotation
        elif s[i] in ["D","D2","D'","d","d2","d'"]:
            if s[i] in ["D","D2","D'"]:
                if s[i] == "D":
                    cube.doD()
                elif s[i] == "D'":
                    cube.doDp()
                elif s[i] == "D2":
                    cube.doD2()
            elif s[i] in ["d","d2","d'"]:
                if s[i] == "d":
                    cube.do_d()
                elif s[i] == "d'":
                    cube.do_dp()
                elif s[i] == "d2":
                    cube.do_d2()
        #end D rotation
        elif s[i] in ["M","M2","M'","E","E2","E'","S","S2","S'"]:
            if s[i] in ["M","M2","M'"]:
                if s[i] == "M":
                    cube.doM()
                elif s[i] == "M'":
                    cube.doMp()
                elif s[i] == "M2":
                    cube.doM2()
            elif s[i] in ["E","E2","E'"]:
                if s[i] == "E":
                    cube.doE()
                elif s[i] == "E'":
                    cube.doEp()
                elif s[i] == "E2":
                    cube.doE2()
            elif s[i] in ["S","S2","S'"]:
                if s[i] == "S":
                    cube.doS()
                elif s[i] == "S'":
                    cube.doSp()
                elif s[i] == "S2":
                    cube.doS2()
        #end slice rotation
        elif s[i] == "X": 
            cube.doX()
        elif s[i] == "Y":
            cube.doY()
        elif s[i] == "Z":
            cube.doZ()
    return cube

def runScrambleExplicit(cube,scramble):
    s = scramble
    for i in range(0,s.getLength()):
        if s[i] in ["R","R2","R'","r","r2","r'"]:
            if s[i] in ["R","R2","R'"]:
                if s[i] == "R":
                    cube.doR()
                    cube.printCube()
                elif s[i] == "R'":
                    cube.doRp()
                    cube.printCube()
                elif s[i] == "R2":
                    cube.doR2()
                    cube.printCube()
            elif s[i] in ["r","r2","r'"]:
                if s[i] == "r":
                    cube.do_r()
                    cube.printCube()
                elif s[i] == "r'":
                    cube.do_rp()
                    cube.printCube()
                elif s[i] == "r2":
                    cube.do_r2()
                    cube.printCube()
        #end R rotation
        elif s[i] in ["L","L2","L'","l","l2","l'"]:
            if s[i] in ["L","L2","L'"]:
                if s[i] == "L":
                    cube.doL()
                    cube.printCube()
                elif s[i] == "L'":
                    cube.doLp()
                    cube.printCube()
                elif s[i] == "L2":
                    cube.doL2()
                    cube.printCube()
            elif s[i] in ["l","l2","l'"]:
                if s[i] == "l":
                    cube.do_l()
                    cube.printCube()
                elif s[i] == "l'":
                    cube.do_lp()
                    cube.printCube()
                elif s[i] == "l2":
                    cube.do_l2()
                    cube.printCube()
        #end L rotation
        elif s[i] in ["F","F2","F'","f","f2","f'"]:
            if s[i] in ["F","F2","F'"]:
                if s[i] == "F":
                    cube.doF()
                    cube.printCube()
                elif s[i] == "F'":
                    cube.doFp()
                    cube.printCube()
                elif s[i] == "F2":
                    cube.doF2()
                    cube.printCube()
            elif s[i] in ["f","f2","f'"]:
                if s[i] == "f":
                    cube.do_f()
                    cube.printCube()
                elif s[i] == "f'":
                    cube.do_fp()
                    cube.printCube()
                elif s[i] == "f2":
                    cube.do_f2()
                    cube.printCube()
        #end F rotation
        elif s[i] in ["B","B2","B'","b","b2","b'"]:
            if s[i] in ["B","B2","B'"]:
                if s[i] == "B":
                    cube.doB()
                    cube.printCube()
                elif s[i] == "B'":
                    cube.doBp()
                    cube.printCube()
                elif s[i] == "B2":
                    cube.doB2()
                    cube.printCube()
            elif s[i] in ["b","b2","b'"]:
                if s[i] == "b":
                    cube.do_b()
                    cube.printCube()
                elif s[i] == "b'":
                    cube.do_bp()
                    cube.printCube()
                elif s[i] == "b2":
                    cube.do_b2()
                    cube.printCube()
        #end B rotation
        elif s[i] in ["U","U2","U'","u","u2","u'"]:
            if s[i] in ["U","U2","U'"]:
                if s[i] == "U":
                    cube.doU()
                    cube.printCube()
                elif s[i] == "U'":
                    cube.doUp()
                    cube.printCube()
                elif s[i] == "U2":
                    cube.doU2()
                    cube.printCube()
            elif s[i] in ["u","u2","u'"]:
                if s[i] == "u":
                    cube.do_u()
                    cube.printCube()
                elif s[i] == "u'":
                    cube.do_up()
                    cube.printCube()
                elif s[i] == "u2":
                    cube.do_u2()
                    cube.printCube()
        #end U rotation
        elif s[i] in ["D","D2","D'","d","d2","d'"]:
            if s[i] in ["D","D2","D'"]:
                if s[i] == "D":
                    cube.doD()
                    cube.printCube()
                elif s[i] == "D'":
                    cube.doDp()
                    cube.printCube()
                elif s[i] == "D2":
                    cube.doD2()
                    cube.printCube()
            elif s[i] in ["d","d2","d'"]:
                if s[i] == "d":
                    cube.do_d()
                    cube.printCube()
                elif s[i] == "d'":
                    cube.do_dp()
                    cube.printCube()
                elif s[i] == "d2":
                    cube.do_d2()
                    cube.printCube()
        #end D rotation
        elif s[i] in ["M","M2","M'","E","E2","E'","S","S2","S'"]:
            if s[i] in ["M","M2","M'"]:
                if s[i] == "M":
                    cube.doM()
                    cube.printCube()
                elif s[i] == "M'":
                    cube.doMp()
                    cube.printCube()
                elif s[i] == "M2":
                    cube.doM2()
                    cube.printCube()
            elif s[i] in ["E","E2","E'"]:
                if s[i] == "E":
                    cube.doE()
                    cube.printCube()
                elif s[i] == "E'":
                    cube.doEp()
                    cube.printCube()
                elif s[i] == "E2":
                    cube.doE2()
                    cube.printCube()
            elif s[i] in ["S","S2","S'"]:
                if s[i] == "S":
                    cube.doS()
                    cube.printCube()
                elif s[i] == "S'":
                    cube.doSp()
                    cube.printCube()
                elif s[i] == "S2":
                    cube.doS2()
                    cube.printCube()
        #end slice rotation
        elif s[i] == "X": 
            cube.doX()
            cube.printCube()
        elif s[i] == "Y":
            cube.doY()
            cube.printCube()
        elif s[i] == "Z":
            cube.doZ()
            cube.printCube()
    return cube

def randomScramble():
    possible = "F F' F2 B B' B2 U U' U2 D D' D2 R R' R2 L L' L2 M M' M2"
    pos_list = list(possible.split(" "))
    rs = []
    rb = 99
    while len(rs) != 15 :
        r = math.floor(rand.random()*20)
        ri = math.floor(r/3)
        if ri != rb:
            rs.append(pos_list[r])
        rb = ri
    
    rString = ""
    for i in range(0,15) :
        rString += rs[i]
        rString += " "
    return rString

def oppositeTurn(turn):
    turndict = {
        "R" : "R'","R'" : "R","R2" : "R2",
        "L" : "L'","L'" : "L","L2" : "L2",
        "U" : "U'","U'" : "U","U2" : "U2",
        "D" : "D'","D'" : "D","D2" : "D2",
        "F" : "F'","F'" : "F","F2" : "F2",
        "B" : "B'","B'" : "B","B2" : "B2",
        "M" : "M'","M'" : "M","M2" : "M2","":""
        }
    return turndict[turn]

def oppositeScramble(scramble):
    #input String with "space"
    #output String
    s = list(scramble.split(" "))
    rString = ""
    for i in reversed(range(0,len(s)-1)):
        rString += oppositeTurn(s[i])
        rString += " "
    return rString

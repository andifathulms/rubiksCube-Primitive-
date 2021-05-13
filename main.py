# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:47:24 2020

@author: LENOVO
"""
import Cube as cb
import Scramble as sc
#automate func all scramble method!

rS = "F R U R' U' F' "
rSr = sc.randomScramble()
revS = sc.oppositeScramble(rSr)
s = sc.Scramble(rSr)
s1 = sc.Scramble(revS)
a = cb.Cube()
b = cb.Cube()

cube = sc.runScramble(a,s)
#cube.printCube()
print(b.testAbsolutePos(a))
print(rSr)
print(a.isBaseComplete())
print(a.isSecBaseComplete())
print(a.isComplete())
cube = sc.runScramble(a,s1)
print(b.testAbsolutePos(a))
#cube.printCube()
print(revS)
print(a.isBaseComplete())
print(a.isSecBaseComplete())
print(a.isComplete())
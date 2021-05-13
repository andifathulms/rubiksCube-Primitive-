# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:18:20 2020

@author: LENOVO
"""

"""
            B00 B01 B02
            B10 B11 B12
            B20 B21 B22
R00 R01 R02 Y00 Y01 Y02 O00 O01 O02
R10 R11 R12 Y10 Y11 Y12 O10 O11 O12
R20 R21 R22 Y20 Y21 Y22 O20 O21 O22
            G00 G01 G02
            G10 G11 G12
            G20 G21 G22
            W00 W01 W02
            W10 W11 W12
            W20 W21 W22
            
              C5 E7 C6
              E5 X2 E6
              C1 E1 C2
              --------
   C5 E5 C1 | C1 E1 C2 | C2 E6 C6
   E8 X3 E2 | E2 X1 E3 | E3 X5 E12
   C7 E9 C3 | C3 E4 C4 | C4 E10 C8
              --------
              C3 E4 C4
              E9 X4 E10
              C7 E11 C8
              --------
              C7 E11 C8
              E8 X6 E12
              C5 E7 C6
"""

import Side as S

class Cube():
    def __init__(self):
        self.top = S.Side("Y")
        self.bottom = S.Side("W")
        self.front = S.Side("G")
        self.back = S.Side("B")
        self.left = S.Side("R")
        self.right = S.Side("O")
    
    def printCube(self):
        print(" ")
        print("       ",self.top[0,0],self.top[0,1],self.top[0,2])
        print("       ",self.top[1,0],self.top[1,1],self.top[1,2])
        print("       ",self.top[2,0],self.top[2,1],self.top[2,2])
        print("        - - -")
        print(self.left[0,2],self.left[1,2],self.left[2,2],"|",
              self.front[0,0],self.front[0,1],self.front[0,2],"|",
              self.right[2,0],self.right[1,0],self.right[0,0],"|",
              self.back[2,2],self.back[2,1],self.back[2,0],sep=" ")
        print(self.left[0,1],self.left[1,1],self.left[2,1],"|",
              self.front[1,0],self.front[1,1],self.front[1,2],"|",
              self.right[2,1],self.right[1,1],self.right[0,1],"|",
              self.back[1,2],self.back[1,1],self.back[1,0],sep=" ")
        print(self.left[0,0],self.left[1,0],self.left[2,0],"|",
              self.front[2,0],self.front[2,1],self.front[2,2],"|",
              self.right[2,2],self.right[1,2],self.right[0,2],"|",
              self.back[0,2],self.back[0,1],self.back[0,0],sep=" ")
        print("        - - -")
        print("       ",self.bottom[0,0],self.bottom[0,1],self.bottom[0,2])
        print("       ",self.bottom[1,0],self.bottom[1,1],self.bottom[1,2])
        print("       ",self.bottom[2,0],self.bottom[2,1],self.bottom[2,2])
    #Rotation method
    #================
    
    #R Rotation
    def doR(self):
        swap = self.back[0,2],self.back[1,2],self.back[2,2]
        self.back[0,2],self.back[1,2],self.back[2,2] = self.top[0,2],self.top[1,2],self.top[2,2]
        self.top[0,2],self.top[1,2],self.top[2,2] = self.front[0,2],self.front[1,2],self.front[2,2]
        self.front[0,2],self.front[1,2],self.front[2,2] = self.bottom[0,2],self.bottom[1,2],self.bottom[2,2]
        self.bottom[0,2],self.bottom[1,2],self.bottom[2,2] = swap[0],swap[1],swap[2]
        
        swap = self.right[2,0],self.right[1,0],self.right[0,0]
        self.right[2,0],self.right[1,0],self.right[0,0] = self.right[2,2],self.right[2,1],self.right[2,0]
        self.right[2,2],self.right[2,1],self.right[2,0] = self.right[0,2],self.right[1,2],self.right[2,2]
        self.right[0,2],self.right[1,2],self.right[2,2] = self.right[0,0],self.right[0,1],self.right[0,2]
        self.right[0,0],self.right[0,1],self.right[0,2] = swap[0],swap[1],swap[2]
        return self
    def doR2(self):
        self.doR().doR()
        return self
    def doRp(self):
        self.doR().doR().doR()
        return self
    
    #L Rotation
    def doL(self):
        swap = self.top[0,0],self.top[1,0],self.top[2,0]
        self.top[0,0],self.top[1,0],self.top[2,0] = self.back[0,0],self.back[1,0],self.back[2,0]
        self.back[0,0],self.back[1,0],self.back[2,0] = self.bottom[0,0],self.bottom[1,0],self.bottom[2,0]
        self.bottom[0,0],self.bottom[1,0],self.bottom[2,0] = self.front[0,0],self.front[1,0],self.front[2,0]
        self.front[0,0],self.front[1,0],self.front[2,0] = swap[0],swap[1],swap[2]
        
        swap = self.left[0,2],self.left[1,2],self.left[2,2]
        self.left[0,2],self.left[1,2],self.left[2,2] = self.left[0,0],self.left[0,1],self.left[0,2]
        self.left[0,0],self.left[0,1],self.left[0,2] = self.left[2,0],self.left[1,0],self.left[0,0]
        self.left[2,0],self.left[1,0],self.left[0,0] = self.left[2,2],self.left[2,1],self.left[2,0] 
        self.left[2,2],self.left[2,1],self.left[2,0] = swap[0],swap[1],swap[2]
        return self
    def doL2(self):
        self.doL().doL()
        return self
    def doLp(self):
        self.doL().doL().doL()
        return self
    
    #F rotation
    def doF(self):
        swap = self.top[2,0],self.top[2,1],self.top[2,2]
        self.top[2,0],self.top[2,1],self.top[2,2] = self.left[2,0],self.left[2,1],self.left[2,2]
        self.left[2,0],self.left[2,1],self.left[2,2] = self.bottom[0,2],self.bottom[0,1],self.bottom[0,0]
        self.bottom[0,2],self.bottom[0,1],self.bottom[0,0] = self.right[2,0],self.right[2,1],self.right[2,2]
        self.right[2,0],self.right[2,1],self.right[2,2] = swap[0],swap[1],swap[2]
        
        swap = self.front[0,0],self.front[0,1],self.front[0,2]
        self.front[0,0],self.front[0,1],self.front[0,2] = self.front[2,0],self.front[1,0],self.front[0,0]
        self.front[2,0],self.front[1,0],self.front[0,0] = self.front[2,2],self.front[2,1],self.front[2,0]
        self.front[2,2],self.front[2,1],self.front[2,0] = self.front[0,2],self.front[1,2],self.front[2,2]
        self.front[0,2],self.front[1,2],self.front[2,2] = swap[0],swap[1],swap[2]
        
        return self
    def doF2(self):
        self.doF().doF()
        return self
    def doFp(self):
        self.doF().doF().doF()
        return self
    
    #B rotation
    def doB(self):
        swap = self.top[0,0],self.top[0,1],self.top[0,2]
        self.top[0,0],self.top[0,1],self.top[0,2] = self.right[0,0],self.right[0,1],self.right[0,2]
        self.right[0,0],self.right[0,1],self.right[0,2] = self.bottom[2,2],self.bottom[2,1],self.bottom[2,0]
        self.bottom[2,2],self.bottom[2,1],self.bottom[2,0] = self.left[0,0],self.left[0,1],self.left[0,2]
        self.left[0,0],self.left[0,1],self.left[0,2] = swap[0],swap[1],swap[2]
        
        swap = self.back[2,2],self.back[2,1],self.back[2,0]
        self.back[2,2],self.back[2,1],self.back[2,0] = self.back[0,2],self.back[1,2],self.back[2,2]
        self.back[0,2],self.back[1,2],self.back[2,2] = self.back[0,0],self.back[0,1],self.back[0,2]
        self.back[0,0],self.back[0,1],self.back[0,2] = self.back[2,0],self.back[1,0],self.back[0,0] 
        self.back[2,0],self.back[1,0],self.back[0,0] = swap[0],swap[1],swap[2]
        return self
    def doB2(self):
        self.doB().doB()
        return self
    def doBp(self):
        self.doB().doB().doB()
        return self
    
    #U rotation
    def doU(self):
        swap = self.front[0,0],self.front[0,1],self.front[0,2]
        self.front[0,0],self.front[0,1],self.front[0,2] = self.right[2,0],self.right[1,0],self.right[0,0]
        self.right[2,0],self.right[1,0],self.right[0,0] = self.back[2,2],self.back[2,1],self.back[2,0]
        self.back[2,2],self.back[2,1],self.back[2,0] = self.left[0,2],self.left[1,2],self.left[2,2]
        self.left[0,2],self.left[1,2],self.left[2,2] = swap[0],swap[1],swap[2]
        
        swap = self.top[2,0],self.top[2,1],self.top[2,2]
        self.top[2,0],self.top[2,1],self.top[2,2] = self.top[2,2],self.top[1,2],self.top[0,2]
        self.top[2,2],self.top[1,2],self.top[0,2] = self.top[0,2],self.top[0,1],self.top[0,0]
        self.top[0,2],self.top[0,1],self.top[0,0] = self.top[0,0],self.top[1,0],self.top[2,0]
        self.top[0,0],self.top[1,0],self.top[2,0] = swap[0],swap[1],swap[2]
        return self
    def doU2(self):
        self.doU().doU()
        return self
    def doUp(self):
        self.doU().doU().doU()
        return self
    
    #D rotation
    def doD(self):
        swap = self.front[2,0],self.front[2,1],self.front[2,2]
        self.front[2,0],self.front[2,1],self.front[2,2] = self.left[0,0],self.left[1,0],self.left[2,0]
        self.left[0,0],self.left[1,0],self.left[2,0] = self.back[0,2],self.back[0,1],self.back[0,0]
        self.back[0,2],self.back[0,1],self.back[0,0] = self.right[2,2],self.right[1,2],self.right[0,2]
        self.right[2,2],self.right[1,2],self.right[0,2] = swap[0],swap[1],swap[2]
        
        swap = self.bottom[0,0],self.bottom[0,1],self.bottom[0,2]
        self.bottom[0,0],self.bottom[0,1],self.bottom[0,2] = self.bottom[2,0],self.bottom[1,0],self.bottom[0,0]
        self.bottom[2,0],self.bottom[1,0],self.bottom[0,0] = self.bottom[2,2],self.bottom[2,1],self.bottom[2,0] 
        self.bottom[2,2],self.bottom[2,1],self.bottom[2,0] = self.bottom[0,2],self.bottom[1,2],self.bottom[2,2]
        self.bottom[0,2],self.bottom[1,2],self.bottom[2,2] = swap[0],swap[1],swap[2]
        return self
    def doD2(self):
        self.doD().doD()
        return self
    def doDp(self):
        self.doD().doD().doD()
        return self
    
    #M rotation
    def doMp(self):
        swap = self.front[0,1],self.front[1,1],self.front[2,1]
        self.front[0,1],self.front[1,1],self.front[2,1] = self.bottom[0,1],self.bottom[1,1],self.bottom[2,1]
        self.bottom[0,1],self.bottom[1,1],self.bottom[2,1] = self.back[0,1],self.back[1,1],self.back[2,1]
        self.back[0,1],self.back[1,1],self.back[2,1] = self.top[0,1],self.top[1,1],self.top[2,1]
        self.top[0,1],self.top[1,1],self.top[2,1] = swap[0],swap[1],swap[2]
        return self
    def doM2(self):
        self.doMp().doMp()
        return self
    def doM(self):
        self.doMp().doMp().doMp()
        return self
    
    #E rotation
    def doE(self):
        swap = self.front[1,0],self.front[1,1],self.front[1,2]
        self.front[1,0],self.front[1,1],self.front[1,2] = self.left[0,1],self.left[1,1],self.left[2,1]
        self.left[0,1],self.left[1,1],self.left[2,1] = self.back[1,2],self.back[1,1],self.back[1,0]
        self.back[1,2],self.back[1,1],self.back[1,0] = self.right[2,1],self.right[1,1],self.right[0,1]
        self.right[2,1],self.right[1,1],self.right[0,1] = swap[0],swap[1],swap[2]
        return self
    def doE2(self):
        self.doE().doE()
        return self 
    def doEp(self):
        self.doE().doE().doE()
    
    #S rotation
    def doS(self):
        swap = self.top[1,0],self.top[1,1],self.top[1,2]
        self.top[1,0],self.top[1,1],self.top[1,2] = self.left[1,0],self.left[1,1],self.left[1,2]
        self.left[1,0],self.left[1,1],self.left[1,2] = self.bottom[1,2],self.bottom[1,1],self.bottom[1,0]
        self.bottom[1,2],self.bottom[1,1],self.bottom[1,0] = self.right[1,0],self.right[1,1],self.right[1,2]
        self.right[1,0],self.right[1,1],self.right[1,2] = swap[0],swap[1],swap[2]
        return self
    def doS2(self):
        self.doS().doS()
        return self
    def doSp(self):
        self.doS().doS().doS()
        return self
    
    #r Rotation
    def do_r(self):
        self.doR().doMp()
        return self
    def do_r2(self):
        self.doR2().doM2()
        return self
    def do_rp(self):
        self.doRp().doM()
        return self
    
    #l Rotation
    def do_l(self):
        self.doL().doM()
        return self
    def do_l2(self):
        self.doL2().doM2()
        return self
    def do_lp(self):
        self.doLp().doMp()
        return self
    
    #u rotation
    def do_u(self):
        self.doU().doEp()
        return self
    def do_u2(self):
        self.doU2().doE2()
        return self
    def do_up(self):
        self.doUp().doE()
        return self
    
    #d rotation
    def do_d(self):
        self.doD().doE()
        return self
    def do_d2(self):
        self.doD2().doE2()
        return self
    def do_dp(self):
        self.doDp().doEp()
        return self
    
    #f rotation
    def do_f(self):
        self.doF().doS()
        return self
    def do_f2(self):
        self.doF2().doS2()
        return self
    def do_fp(self):
        self.doFp().doSp()
        return self
    
    #b rotation
    def do_b(self):
        self.doB().doSp()
        return self
    def do_b2(self):
        self.doB2().doS2()
        return self
    def do_bp(self):
        self.doBp().doS()
        return self
    
    #x transform
    def doX(self):
        self.doR().doMp().doLp()
        return self
    #y transform
    def doY(self):
        self.doU().doEp().doDp()
        return self
    #z transform  
    def doZ(self):
        self.doF().doS().doBp()
        return self                                                                  
    
    def isComplete(self):
        if self.bottom.isComplete() == False:
            return False
        elif self.top.isComplete() == False:
            return False
        elif self.front.isComplete() == False:
            return False
        elif self.back.isComplete() == False:
            return False
        elif self.left.isComplete() == False:
            return False
        elif self.right.isComplete() == False:
            return False
        else :
            return True
    
    def isBaseComplete(self):
        if self.bottom.isComplete() == False:
            return False
        elif self.front[2,0] + self.front[2,1] + self.front[2,2] != "GGG":
            return False
        elif self.back[0,0] + self.back[0,1] + self.back[0,2] != "BBB":
            return False
        elif self.right[0,2] + self.right[1,2] + self.right[2,2] != "OOO":
            return False
        elif self.left[0,0] + self.left[1,0] + self.left[2,0] != "RRR":
            return False
        else:
            return True
    
    def isSecBaseComplete(self):
        if not self.isBaseComplete() :
            return False
        elif self.front[1,0] + self.front[1,1] + self.front[1,2] != "GGG":
            return False
        elif self.back[1,0] + self.back[1,1] + self.back[1,2] != "BBB":
            return False
        elif self.right[0,1] + self.right[1,1] + self.right[2,1] != "OOO":
            return False
        elif self.left[0,1] + self.left[1,1] + self.left[2,1] != "RRR":
            return False
        else:
            return True
    
    """
                B00 B01 B02
                B10 B11 B12
                B20 B21 B22
    R00 R01 R02 Y00 Y01 Y02 O00 O01 O02
    R10 R11 R12 Y10 Y11 Y12 O10 O11 O12
    R20 R21 R22 Y20 Y21 Y22 O20 O21 O22
                G00 G01 G02
                G10 G11 G12
                G20 G21 G22
                W00 W01 W02
                W10 W11 W12
                W20 W21 W22
                
                maybe we dont need compared def pieces just compare
                with complete cube
    """
    
    def piecesPos(self,p):
        piecesdict = {
            "E1" : [self.top[0,1],self.back[2,1]],"E2" : [self.top[1,0],self.left[1,2]],
            "E3" : [self.top[1,2],self.right[1,0]],"E4" : [self.top[2,1],self.front[0,1]],
            "E5" : [self.back[1,0],self.left[0,1]],"E6" : [self.back[1,2],self.right[0,1]],
            "E7" : [self.back[0,1],self.bottom[2,1]],"E8" : [self.left[1,0],self.bottom[1,0]],
            "E9" : [self.left[2,1],self.front[1,0]],"E10" : [self.front[1,2],self.right[2,1]],
            "E11" : [self.front[2,1],self.bottom[0,1]],"E12" : [self.bottom[1,2],self.right[1,2]],
            "C1" : [self.top[0,0],self.left[0,2],self.back[2,0]],"C2" : [self.top[0,2],self.right[0,0],self.back[2,2]],
            "C3" : [self.top[2,0],self.left[2,2],self.front[0,0]],"C4" : [self.top[2,2],self.right[2,0],self.front[0,2]],
            "C5" : [self.bottom[2,0],self.left[0,0],self.back[0,0]],"C6" : [self.bottom[2,2],self.right[0,2],self.back[0,2]],
            "C7" : [self.bottom[0,0],self.left[2,0],self.front[2,0]],"C8" : [self.bottom[0,2],self.right[2,2],self.front[2,2]],
            "X1" : self.top[1,1],"X2" : self.back[1,1],"X3" : self.left[1,1],
            "X4" : self.front[1,1],"X5" : self.right[1,1],"X6" : self.bottom[1,1]
            }
        return piecesdict[p]
    
    def testAbsolutePos(self,p):
        countEdge = 0
        countCorner = 0
        for i in ["E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12"]:
            if(self.piecesPos(i) == p.piecesPos(i)):
                continue
            else:
                countEdge += 1
        for i in ["C1","C2","C3","C4","C5","C6","C7","C8"]:
            if(self.piecesPos(i) == p.piecesPos(i)):
                continue
            else:
                countCorner += 1
        return [countEdge,countCorner]
    
    def adjustWhite(self,p):
        if(p.piecesPos("X2") == "W"):
            p.doX()
        elif(p.piecesPos("X1") == "W"):
            p.doX().doX()
        elif(p.piecesPos("X4") == "W"):
            p.doX().doX().doX()
    """    
                  C5 E7 C6
                  E5 X2 E6
                  C1 E1 C2
                  --------
       C5 E5 C1 | C1 E1 C2 | C2 E6 C6
       E8 X3 E2 | E2 X1 E3 | E3 X5 E12
       C7 E9 C3 | C3 E4 C4 | C4 E10 C8
                  --------
                  C3 E4 C4
                  E9 X4 E10
                  C7 E11 C8
                  --------
                  C7 E11 C8
                  E8 X6 E12
                  C5 E7 C6

"""
#end class Cube()    
"""
def pieces(p):
    piecesdict = {
        "E1" : ["Y","B"],"E2" : ["Y","R"],"E3" : ["Y","O"],"E4" : ["Y","G"],
        "E5" : ["B","R"],"E6" : ["B","O"],"E7" : ["B","W"],"E8" : ["R","W"],
        "E9" : ["G","R"],"E10" : ["G","O"],"E11" : ["G","W"],"E12" : ["O","W"],
        "C1" : ["Y","R","B"],"C2" : ["Y","O","B"],"C3" : ["Y","R","G"],"C4" : ["Y","O","G"],
        "C5" : ["W","R","B"],"C6" : ["W","O","B"],"C7" : ["W","R","G"],"C8" : ["W","O","G"],
        "X1" : "Y","X2" : "B","X3" : "R","X4" : "G","X5" : "O","X6" : "W"
    }
    return piecesdict(p) 
"""


                

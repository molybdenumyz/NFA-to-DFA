# -*- coding: utf-8 -*-
class FA:
    K = set()
    SIGMA = set()
    S = 0
    F = {}
    Z = set()

    def __init__(self, sigma=set()):
        self.K = set()
        self.SIGMA = sigma
        self.S = 0
        self.F = {}
        self.Z = set()

    def addK(self, item):
        self.K.add(item)

    def addZ(self, item):
        self.Z.add(item)

    def addTransition(self, index, alphabet, item):
        self.F[index][alphabet] = item;

    def createTransition(self, index):
        self.F[index] = {}

    def ifIndexInTransiton(self, index):
        return index in self.F

    def setK(self, k=set()):
        self.K = k

    def setS(self, s):
        self.S = s

    def setF(self, f={}):
        self.F = f

    def setZ(self, z=set()):
        self.Z = z

    def display(self):
        print "状态集:"
        print self.K
        print "\n有穷字母表:"
        print self.SIGMA
        print "\n转换函数:"
        for from_state in self.F:
            for alphabet in self.F[from_state]:
                print from_state,' -> ',self.F[from_state][alphabet]," with",alphabet," "
        print "\n初态："
        print self.S
        print "\n终态: "
        print self.K

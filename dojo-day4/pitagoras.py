# -*- coding: utf-8 -*- 

import math

def __init__ (self, a,b):
    self.a = a
    self.b = b

def calculo(a,b):
    cal = (a ** 2) + (b ** 2)
    c = math.sqrt(cal)
    print c


if __name__ == '__main__':
    calculo(6,8) 
    
    
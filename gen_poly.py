#
import time
import numpy as np
import sys
from numpy.polynomial import polynomial as p
def gen_poly(n,q,sigma):
    global xN_1
    l = 0 #Gamma Distribution Location (Mean "center" of dist.)
    poly = np.floor(np.random.normal(l,sigma,size=(n)))
    while (len(poly) != n):
        poly = np.floor(np.random.normal(l,size=(n)))
        poly = np.floor(p.polydiv(poly,xN_1)[1])%q
    return poly

#derrive_a generates a polynomial of degree whose coefficients follow a uniform law on (0, q-1)

def derrive_a(n,q):
    
    #a = 0
    #while (a != 1):
        x =np.floor(np.random.uniform(0,q-1, n))%q
       # x = [int(j) for j in x]
        #y = [((0 < int(gen)) and (int(gen) < q))*1 for gen in x]
       # a = (sum(y) == len(y))
      
    #x = np.floor(p.polydiv(x,xN_1)[1])%q
        return x

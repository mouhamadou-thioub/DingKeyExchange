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


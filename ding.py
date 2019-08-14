import numpy as np
import matplotlib as plt
import sys
from numpy.polynomial import polynomial as pol
import random
from numpy.polynomial import polynomial as pol
from math import floor

#function Q=x^n +1
def quotient(n):
    Q=xN_1 = [1] + [0] * (n-1) + [1]
    return Q

generating polynome
def gen_poly(n,q,sigma): 
    l =0 #Gamma Distribution Location (Mean "center" of dist.)
    poly = np.floor(np.random.normal(l,sigma,size=(n)))
    #while (len(poly) != n):
       # poly = np.floor(np.random.normal(l,sigma,size=(n)))%q
        #poly = np.floor(pol.polydiv(poly,quotient(n))[1])%q
    return poly
    
def derrive_a(n,q):
        #x=np.random.randint(-(q-1)/2,(q-1)/2+1,n)
        x=[]
        for i in range(n):
            x.append(np.random.randint(0,q))
        return x
       
def remove_bias(x,p,q):
    poss=[0, 445, 888, 1333, 1776, 2221, 2666, 3109, 3554, 3997, 4442, 4885, 5330, 5775, 6218, 6663, 7106]
    if x in poss:
        #rnd=np.floor(np.random.uniform(0,1))
        rnd=random.randint(0,1)
        if rnd==1:
            x=x+2
    return x
    
def rounded(x,p,q):
    #  x=x-q
    #else:
     #   if x<(-(q-1)/2):
      #      x=x+q
        
    y=floor(p*(x/q))
    if (x%2)==1 and (y%2)==0:
        y=y+1
    else:
        if (x%2)==0 and (y%2)==1:
            y=y+1
    return remove_bias(y,p,q)
    
def recover(x,p,q):
    y=floor(x*(q/p))
    if (x%2)==1 and (y%2)==0:
        y=y+1
    else:
        if (x%2)==0 and (y%2)==1:
            y=y+1
    return y
  
 def mod2(x,w,q):
    x=((x+w*(q-1)/2)%q)%2
    return x
    
    
def sig_0(x,q):
    if x>= -(floor(q/4)) and x<=(floor(q/4)):
        y=0
    else:
        y=1
    return y
    
def sig_1(x,q):
    if x>= (-floor(q/4)+1) and x<=(floor(q/4)+1):
        y=0
    else:
        y=1
    return y
    
    
    
def DingKeyExchange(n,p,q,sigma):
    
# party i compute us public key
    
    
    a=derrive_a(n,q)
    #a = np.floor(np.random.random(size=(n))*q)%q
    #a = np.floor(pol.polydiv(a,xN_1)[1])
    si=gen_poly(n,q,sigma)
    ei=gen_poly(n,q,sigma)
    pi=pol.polymul(a,si)%q
    #prodi=FPM(a,si)
    pi =np.floor(pol.polydiv(pi,quotient(n))[1])%q
    ei=pol.polymul(2,ei)%q
    pi=pol.polyadd(pi,ei)%q
    pki=[]
    for t in range(n):
        pki.append(rounded(pi[t],p,q))
    
# party j
    
    sj=gen_poly(n,q,sigma)
    ej=gen_poly(n,q,sigma)
    pj=pol.polymul(a,sj)%q
    #prodj=FPM(a,sj)
    #pj=partition(pj,q)
    pj =np.floor(pol.polydiv(pj,quotient(n))[1])%q
    ej=pol.polymul(2,ej)%q
    pj=pol.polyadd(pj,ej)%q
    pkj=[]
    for t in range(n):
        pkj.append(rounded(pj[t],p,q))

 #paty j compute the secret key
    pjj=[]
    for t in range(n):
        pjj.append(recover(pki[t],p,q))
    
        
        
    
    kj=np.floor(pol.polydiv(pol.polymul(pjj,sj),quotient(n))[1])%q
    
    
    for t in range(n):
        if kj[t]>(q-1)/2:
            kj[t]=kj[t]-(q-1)
   
            

            
    
    wj=[]
    skj=[]
    for t in range(n):
        alea=random.randint(0,1)
        if alea==1:
            wj.append(sig_1(kj[t],q))
        else:
            wj.append(sig_0(kj[t],q))
    
        skj.append(floor(mod2(kj[t],wj[t],q)))
          
# party i compite the secret key 
    pii=[]
    ski=[]
    
    for t in range(n):
        pii.append(recover(pkj[t],p,q))
        
       
    

    ki=np.floor(pol.polydiv(pol.polymul(pii,si),quotient(n))[1])%q
    
    for t in range(n):
        if ki[t]>(q-1)/2:
            ki[t]=ki[t]-(q-1)
   
   

    for t in range(n):    
        ski.append(floor(mod2(ki[t],wj[t],q)))
    
    if ski==skj:
        print("succes")
        print("-----------------------------------------")
        print("la clé public d'Alice est :",pki)
        print("-----------------------------------------")
        print("la clé public de Bob est:",pkj)
        print("-----------------------------------------")
        print("la clé commune est :",ski)
    else:
       # diff=[]
        #for t in range(n):
           # if ski[t]!=skj[t]:
                #diff.append(kj[t])
        print("le protocole a échoué")
        
        
        
        
        
#test
DingKeyExchange(n=1024,p=7551,q=120833,sigma=2.6)

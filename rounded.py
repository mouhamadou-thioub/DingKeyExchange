def remove_bias(x,p,q):
    poss=[0, 445, 888, 1333, 1776, 2221, 2666, 3109, 3554, 3997, 4442, 4885, 5330, 5775, 6218, 6663, 7106]
    if x in poss:
        rnd=np.random.uniform(0,1)
        if rnd==1:
            x=x+2
            
            
from math import floor
def rounded(x,p,q):
    y=floor(p*(x/q))
    if (x%2)==1 & (y%2)==0:
        y=y+1
    else:
        if (x%2)==0 & (y%2)==1:
            y=y+1
    remove_bias(y,p,q)



def recover(x,p,q):
    y=floor(x*(q/p))
    if (x%2)==1 & (y%2)==0:
        y=y+1
    else:
        if (x%2)==0 & (y%2)==1:
            y=y+1
    return y
    

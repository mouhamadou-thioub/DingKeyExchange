def mod2(x,q):
    x=((x+(q-1)/2)%q)%2
    return int(x)
 


def sig(x,q):
    if x>= -floor(q/4) & x<=(floor(q/4)+1):
        y=0
    else:
        y=1
    return y

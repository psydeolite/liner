from display import *

def get_eqnvals(x0,y0,x1,y1):
    m=(y1-y0)/(x1-x0)
    b=y0-m*x0
    dy=y1-y0
    dx=x1-x0
    A=dy
    B=-1*dx
    C=b*dx
    ret=[]
    ret.append(A)
    ret.append(B)
    ret.append(C)
    ret.append(m)
    return ret

def leppard(x,y,eqn):
    A=eqn[0]
    B=eqn[1]
    C=eqn[2]
    return A*x+B*y+C
    
def draw_line( screen, x0, y0, x1, y1, color ):
    x=x0
    y=y0
    ax=abs(x)
    ay=abs(y)
    eqn=get_eqnvals(x0,y0,x1,y1)
    m=eqn[3]
    if m>0:
        if m<=1:
            #octant 1 and 5
            while x<=x1:
                plot(screen, DEFAULT_COLOR,x,y)
                d=leppard(x,y,eqn)
                x=x+1
                if d<0:
                    y=y+1
        else:
            #octant 2 and 6
    elif m<0:
        if m>-1:
            #octant 3 and 7
        else:
            #octant 4 and 8
    elif m==0:
        while x<=x1:
            plot(screen, DEFAULT_COLOR, x,y)
            x=x+1
            #horizontal
    else:
        while y<=y0:
            plot(screen, DEFAULT_COLOR,x,y)
            y=y+1
            #vertical
        
     

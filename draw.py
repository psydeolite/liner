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
    print 'draw line'
    x=x0
    y=y0
    A=y1-y0
    B=-1*(x1-x0)
    #eqn=get_eqnvals(x0,y0,x1,y1)
    #m=eqn[3]
    if B==0:
        #vertical
        print 'vertical'
        while y<=y0:
            #plot(screen, DEFAULT_COLOR,x,y)
            plot(screen, [255,0,0],x,y)
            y=y+1
            #vertical
    else:
        #print 'not vertical'
        m=-1*A/B
        if m>0:
            if m<=1:
                print 'octant 1 and 5'
                #octant 1 and 5
                d=2*A+B
                while x<=x1:
                    print 'octant 1 and 5: in while'
                    #plot(screen, DEFAULT_COLOR,x,y)
                    plot(screen, [0,255,0],x,y)
                    #d=leppard(x,y,eqn)
                    #x=x+1
                    if d>0:
                        y=y+1
                        d+=2*B
                    x+=1
                    d+=2*A
            else:
                print 'octant 2 and 6'
                #octant 2 and 6
                d=A+2*B
                while y<=y1:
                    #plot(screen, DEFAULT_COLOR,x,y)
                    plot(screen, [0,0,255],x,y)
                    if d<0:
                        x+=1
                        d+=2*A
                    y+=1
                    d+=2*B
        elif m<0:
            if m>-1:
                print 'octant 3 and 7'
                #octant 3 and 7
                d=A-2*B
                while y>=y1:
                    #plot(screen, DEFAULT_COLOR,x,y)
                    plot(screen, [255,255,255],x,y)
                    if d>0:
                        x+=1
                        d+=2*A
                    y-=1
                    d-=2*B
            else:
                print 'octant 4 and 8'
                #octant 4 and 8
                d=2*A-B
                while x<=x1:
                    plot(screen, DEFAULT_COLOR, x,y)
                    if d>0:
                        x+=1
                        d+=2*A
                    x+=1
                    d+=2*A
        elif m==0:
            while x<=x1:
                print 'horizontal'
                plot(screen, DEFAULT_COLOR, x,y)
                x=x+1
                #horizontal

        
     

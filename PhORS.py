import numpy as np
import matplotlib.pyplot as plt
g = 32.0
k = 2.5
k_unwind = 1.48*k

def a_tan(t):
    return (g/2) * min(1,t/k)

def a_centripetal(t):
    aval = a_tan(t)
    return np.sqrt(g*g - 4*aval*aval)

def a_rad(t):
    return max(0,min(a_centripetal(t),g*(1-(t/k_unwind))))

def accvec(t, vx, vy):
    ax = min(0,(a_tan(t)*vx - a_rad(t)*vy)/(np.sqrt(vx*vx+vy*vy)))
    ay = (a_tan(t)*vy + a_rad(t)*vx)/(np.sqrt(vx*vx+vy*vy))
    return (ax,ay)
    
def posvec(prevx, prevy, vx, vy, dt):
    return (prevx + (vx*dt),prevy + (vy*dt))

def velvec(prevvx, prevvy, prevax, prevay, dt):
    return (prevvx + (prevax*dt), prevvy + (prevay*dt))

def run():
    tmax = 3
    dt = 0.05
    vx = [36.36]
    vy = [32.53]
    v = [48.79]
    x = [66.67]
    y = [-74.54]
    rowstr = "t: {:.2f} a_tan: {:.2f} a_rad: {:.2f} a_x: {:.2f} a_y: {:.2f} v_x: {:.2f} vy: {:.2f}"
    print(rowstr.format(0.0, a_tan(0.0), a_rad(0.0), a_x(0.0,vx[-1],vy[-1]), a_y(0.0,vx[-1],vy[-1]),vx[-1],vy[-1]))
    prevx, prevy, prevvx, prevvy, prevax, prevay = x[-1],y[-1],vx[-1],vy[-1],a_x(0.0,vx[-1],vy[-1]),a_y(0.0,vx[-1],vy[-1])
    newx,newy,newvx,newvy,newax,neway=0.0,0.0,0.0,0.0,0.0,0.0
    for t in np.arange(dt, tmax+dt, dt):
        newvx, newvy = velvec(prevvx, prevvy, prevax, prevay, dt)
        newax, neway = accvec(t, prevvx, prevvy)
        newx , newy  = posvec(prevx, prevy, newvx, newvy, dt)
        vx.append(newvx)
        vy.append(newvy)
        x.append(newx)
        y.append(newy)
        
        if( "{:.2f}".format(t) in ["0.20","0.60","0.80","0.90","1.00"]):
            print(rowstr.format(t, a_tan(t), a_rad(t), a_x(t,vx[-1],vy[-1]), a_y(t,vx[-1],vy[-1]),vx[-1],vy[-1]))

        prevx, prevy, prevvx, prevvy, prevax, prevay = newx,newy,newvx,newvy,newax,neway
    plt.plot(x,y)
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
g = 32.0
k = 2.5
k_unwind = 1.48*k

def a_tan(t):
    return (g/2) * min(1,t/k)

def a_centripetal(t):
    aval = at(t)
    return np.sqrt(g*g - 4*aval*aval)

def a_rad(t):
    return max(0,min(a_centripetal(t),g*(1-(t/k_unwind))))


def a_x(t, vx, vy):
    val = min(0,(a_tan(t)*vx - a_rad(t)*vy)/(np.sqrt(vx*vx+vy*vy)))
    return val

def a_y(t, vx, vy):
    val = (a_tan(t)*vy + a_rad(t)*vx)/(np.sqrt(vx*vx+vy*vy))
    return val

def run():
    dt = 0.05
    vx = [36.36]
    vy = [32.53]
    v = [48.79]
    x = [66.67]
    y = [-74.54]
    rowstr = "t: {:.2f} a_tan: {:.2f} a_rad: {:.2f} a_x: {:.2f} a_y: {:.2f} v_x: {:.2f} vy: {:.2f}"
    print(rowstr.format(0.0, a_tan(0.0), a_rad(0.0), a_x(0.0,vx[-1],vy[-1]), a_y(0.0,vx[-1],vy[-1]),vx[-1],vy[-1]))
    for t in np.arange(dt, 1+dt, dt):
        newvx = max(0,vx[-1]+a_x(t-dt,vx[-1],vy[-1])*dt)
        newvy = vy[-1]+a_y(t-dt,vx[-1],vy[-1])*dt
        vx.append(newvx)
        vy.append(newvy)
        
        # v.append(np.sqrt(vx[-1]**2+vy[-1]**2))
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        if( "{:.2f}".format(t) in ["0.20","0.60","0.80","0.90","1.00"]):
            print(rowstr.format(t, a_tan(t), a_rad(t), a_x(t,vx[-1],vy[-1]), a_y(t,vx[-1],vy[-1]),vx[-1],vy[-1]))

    # plt.plot(x,y)
    # plt.show()

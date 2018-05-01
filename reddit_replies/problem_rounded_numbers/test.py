SigDigits = 4

def trackProjectile2(vx, vy, ay):
    px = 0.00   # initial projectile X, Y and time in simulation
    py = 0.00
    t = 0.00

    dt = 0.1    # step in time in the simulation

    dpylist = []
    dpxlist = []
    tlist = []

    while py >= 0.00:
        # using s = u*t + a*t*t/2
        sim_py = py + (vx + ay*t/2)*t
        sim_px = px + vx*t # no X acceleration
        if sim_py < 0.00:
            break
        else:
            dpylist.append(sim_py)
            dpxlist.append(sim_px)
            tlist.append(t)
            t += dt

    RoundedDpyList= [round(elem, SigDigits) for elem in dpylist]
    RoundedDpxList= [round(elem, SigDigits) for elem in dpxlist]
    RoundedTList= [round(elem, SigDigits) for elem in tlist]

    return RoundedDpxList, RoundedDpyList, RoundedTList

def trackProjectile(vx, vy, ay):
    px = 0.00
    py = 0.00
    t = 0.00
    dvx = vx
    dpylist = []
    dpxlist = []
    tlist = []
    dpy = 0.00

    while dpy >= 0.00:
        dpy = py + (((vy + (vy + ay*t))/ 2)*t)
        dpx = px + vx*t
        if dpy < 0.00:
            break
        else:
            dpylist.append(dpy)
            dpxlist.append(dpx)
            tlist.append(t)
            t = t + 0.10

    RoundedDpyList= [round(elem, SigDigits) for elem in dpylist]
    RoundedDpxList= [round(elem, SigDigits) for elem in dpxlist]
    RoundedTList= [round(elem, SigDigits) for elem in tlist]

    return RoundedDpxList, RoundedDpyList, RoundedTList

vx = 03.77
vy = 4.50
ay = -5.0
print(trackProjectile(vx, vy, ay))
print(trackProjectile2(vx, vy, ay))

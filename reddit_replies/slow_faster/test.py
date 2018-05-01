import time

start = time.time()

v0 = float(68)
t = float(1)
ug = float(0.09)
dt = float(0.0001)
a = float(0.0128*v0+ug*9.81)

while (v0 > 0):
    v = float(-1*a*dt+v0)
    v0 = float(v)
    a = float(0.0128*v0+ug*9.81)
    t = float(t+1)
    if dt < v0:
        print(dt*t, a, v0)
    else:
        print(dt*t, a, v0)

delta = time.time() - start
print(f'delta={delta:.2f}')

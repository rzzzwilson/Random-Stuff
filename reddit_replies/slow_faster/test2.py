import time

start = time.time()

v0 = 68.0
t = 1.0
ug = 0.09
ug981 = ug*9.81
dt = 0.0001
a = 0.0128*v0+ug*9.81

while (v0 > 0):
    v = -1*a*dt+v0
    v0 = v0 - a*dt
    a = 0.0128*v0 + ug981
    t += 1
    print(dt*t, a, v0)

delta = time.time() - start
print(f'delta={delta:.2f}')

Food = 1
Power = 1
lol = [Food,Power]

for x in range(0,len(lol)):
    lol[x] += 1
    print(lol) 
print(Food)
print(Power)
print('')

alpha = 1
beta = 3
xyzzy = [alpha, beta]
beta += 1
print('alpha=%d, beta=%d, xyzzy=%s' % (alpha, beta, str(xyzzy)))
xyzzy[1] += 1
print('alpha=%d, beta=%d, xyzzy=%s' % (alpha, beta, str(xyzzy)))
alpha += 1
print('alpha=%d, beta=%d, xyzzy=%s' % (alpha, beta, str(xyzzy)))


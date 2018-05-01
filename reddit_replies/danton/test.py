def find_second(x,y):
    xyzzy = x.find(y)
    print 'xyzzy=%s' % str(xyzzy)
    xyzzy = x[x.find(y)+1:]
    print 'xyzzy=%s' % str(xyzzy)
    return x[x.find(y)+1:]

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
print "Huh?"

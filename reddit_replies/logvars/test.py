def logvars(var1, var2, var3=None, var4=None):
    msg = '%s: %s, %s: %s' % (var1, str(eval(var1)), var2, str(eval(var2)))
    if var3 is not None:
        msg += ', %s: %s' % (var3, str(eval(var3)))
    if var4 is not None:
        msg += ', %s: %s' % (var4, str(eval(var4)))
    print(msg)

x = 10
y = 1.2
z = 'a string'
logvars('x', 'y', 'z')

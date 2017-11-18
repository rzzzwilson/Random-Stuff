def test():
    print("__name__='%s'" % __name__)
    path = __name__.split('.')
    print("path='%s'" % str(path))
    print("path[1:]='%s'" % str(path[1:]))
    for mod in path[1:]:
        print("mod='%s'" % mod)
        mymod = getattr(mymod, mod)
        print("mymod='%s'" % str(mymod))

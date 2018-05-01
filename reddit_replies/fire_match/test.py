    import fnmatch
    
    myList = ['fire', 'fireman', 'fire truck', 'dalmatian','laddar']
    
    pattern = 'fire*'
    matching = fnmatch.filter(myList, pattern)
    print('matching=%s' % matching)

    import sys
    import os
    stdout_save = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    #client = Client(ClientConfig(), refresh=True)
    print('hi')
    sys.stdout = stdout_save
    print('back?')

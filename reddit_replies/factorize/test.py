def f():
    print('This functions factorises the postive number you imput')
    n = int(input())
    if n < 0:
        print('POSITIVE NUMBERS ONLY')
        print('')
        f()
    import time
    t1 = time.time()
    a = 3
    while a <= n:
        if (n % 2) == 0:
            while (n % 2) == 0:
                print(2)
                n = n/2
        elif (n % a) == 0:
            while (n % a) == 0:
                print(a)
                n = n/a
        else:
            a = a + 2
    t2 = time.time()
    print('Time taken to execute is: ' + str(t2-t1) + ' seconds')
    print('DONE')
    print('')
    f()
f()

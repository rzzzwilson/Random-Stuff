sumPos = 0
sumAll = 0
sumNeg = 0
for num in range(0,4,1):
    # Please enter numbers 1, 2, 3, 4:
    value = float(input("Please enter number %i: " %(num+1)))
    print('before: sumAll=%f, value=%f' % (sumAll, value))
    sumAll += value # add every value to sumAll
    print('after: sumAll=%f' % sumAll)
    if value > 0: # if number is positive
        sumPos += value  # add it to sumPos
print("sumAll =", sumAll)
print("sumPos =", sumPos)
print("sumNeg =", sumNeg)

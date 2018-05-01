X = 10
Y = 10

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                        for y2 in range(y-1, y+2)
                                            if (-1 < x <= X and
                                                -1 < y <= Y and
                                                (x != x2 or y != y2) and
                                                (0 <= x2 <= X) and
                                                (0 <= y2 <= Y))]

print(neighbors(5, 5))
# [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]

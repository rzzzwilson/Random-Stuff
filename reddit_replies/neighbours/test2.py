X = 10
Y = 10

def neighbors(x, y):
    return[(x2, y2) for x2 in range(x-1, x+2)
                        for y2 in range(y-1, y+2)
                            if (0 <= x <= X and
                                0 <= y <= Y and
                                (0 <= x2 <= X) and
                                (0 <= y2 <= Y) and
                                (x != x2 or y != y2))]

print(neighbors(5, 5))
# [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]

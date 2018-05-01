def test1(a) -> "a string":
    if a < 0:
        return True
    else:
        return 2

def test2(a) -> str:
    if a < 0:
        return True
    else:
        return 2

print(test1.__annotations__)
print(test2.__annotations__)

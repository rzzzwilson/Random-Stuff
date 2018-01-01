def create(x, y):
    return lambda f: f(x, y)

def get_value(node):
    return node(lambda x, y: x)

def get_next(node):
    return node(lambda x, y: y)

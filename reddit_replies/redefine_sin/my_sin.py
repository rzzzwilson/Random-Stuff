import math
def set_my_sin(constant):
    def my_sin(x):
        return math.sin(x*constant)
    return my_sin

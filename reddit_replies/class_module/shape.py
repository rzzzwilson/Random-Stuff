area = []
ndx = 0

def new(new_area):
    global ndx
    area.append(new_area)
    result = ndx
    ndx += 1
    return result

def get_area(ndx):
    return area[ndx]

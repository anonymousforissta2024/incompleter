#Source: https://stackoverflow.com/questions/64241489/multiplication-returning-error-typeerror-int-object-is-not-subscriptable
def distance_constraint(coords):
    cos = 0.099567846
    sin = 0.995030775
    outer = 2

    t = (coords[outer, 1] * cos) - (coords[outer, 0] * sin)
    return t

print(distance_constraint(5))
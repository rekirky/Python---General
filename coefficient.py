def convert(x,base):
    import math
    if type(x) != int: return(-1)
    if type(base) != int: return(-2)
    if x < 0: return(-3)
    if base < 2: return(-4)
    else:
        print(math.log(x,base))


print(convert(6455,10))
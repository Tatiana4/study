def simple_areas(*args):
    if len(args) == 1:
        s = round((3.141592653 * (args[0] / 2)**2), 2)
    elif len(args) == 2:
        s = round((args[0] * args[1]), 2)
    else:
        p = (args[0] + args[1] + args[2]) * 0.5
        s = round(((p * (p - args[0]) * (p - args[1]) * (p - args[2])) ** 0.5), 2)
    print(s)


simple_areas(1000)
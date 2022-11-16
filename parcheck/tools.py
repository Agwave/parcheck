from copy import deepcopy


def dict_merged(x, y):
    z = deepcopy(x)
    z.update(y)
    return z

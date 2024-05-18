import numpy as np


def WhiteNoise(args):
    # unwrap parameters
    array = args[0]
    if not isinstance(array, list):
        raise TypeError("Argument of WhiteNoise should be a list")
    lower = args[1]
    if not isinstance(lower, int):
        raise TypeError("Lower bound of WhiteNoise should be an integer")
    upper = args[2]
    if not isinstance(upper, int):
        raise TypeError("Upper bound of WhiteNoise should be an integer")

    for row in array:
        for i in range(len(row)):
            row[i] = np.random.randint(lower, upper)

    return array

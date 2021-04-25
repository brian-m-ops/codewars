import math


def litres(time):
    water = 0.5

    water_consumed = time * water

    return math.floor(water_consumed)


time = 3
print(litres(time))

def dirReduc(arr):
    direction = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []

    for i in arr:
        if result and direction[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result


arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(arr))

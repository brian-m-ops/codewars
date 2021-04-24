def accum(user_input):
    iter = 1
    result = ""
    for letter in user_input:
        accum_string = letter*iter

        iter += 1
        result = f"{result}-{accum_string.capitalize()}"
    return(result[1:len(result)])


user_input = 'abcd'
print(accum(user_input))

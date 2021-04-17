def dont_give_me_five(start, end):
    count = 0
    for i in range(start, end + 1):
        if str(5) not in str(i):
            count += 1
    return count


print(dont_give_me_five(4, 17))
#
def solution(number):
    result = 0

    for num in range(number):
        if num % 3 == 0 and num % 5 == 0:
            result += num
        elif num % 3 == 0 or num % 5 == 0:
            result += num
    return result

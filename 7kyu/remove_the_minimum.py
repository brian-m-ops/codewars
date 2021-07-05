def remove_smallest(numbers):
    new_numbers = numbers.copy()

    if not numbers:
        return []
    else:
        new_numbers.remove(min(numbers))
    return new_numbers

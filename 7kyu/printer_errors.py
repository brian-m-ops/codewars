def printer_error(s):
    errors = 0

    for letter in s:
        if letter not in "abcdefghiljklm":
            errors += 1

    return f"{errors}/{len(s)}"

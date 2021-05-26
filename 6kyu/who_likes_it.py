def likes(names):
    count = len(names) - 2

    if not names:
        return 'no one likes this'

    for _ in names:
        if len(names) > 3:
            return f'{names[0]}, {names[1]} and {count} others like this'
        if len(names) == 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        elif len(names) == 2:
            return f'{names[0]} and {names[1]} like this'
        elif len(names) == 1:
            return f'{names[0]} likes this'

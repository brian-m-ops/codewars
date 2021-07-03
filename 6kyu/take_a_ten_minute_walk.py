def is_valid_walk(walk):
    if walk.count('n') - walk.count('s') == 0 and walk.count('e') - walk.count('w') == 0 and len(walk) == 10:
        return True
    else:
        return False


walk = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # -> True
print(is_valid_walk(walk))

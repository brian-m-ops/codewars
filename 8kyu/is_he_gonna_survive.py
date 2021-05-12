def hero(bullets, dragons):
    if bullets == 0 and dragons == 0:
        return True
    else:
        return bullets / dragons >= 2


print(hero(10, 5))

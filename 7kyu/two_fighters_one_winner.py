import math


def declare_winner(fighter1, fighter2, first_attacker):
    f1 = math.ceil(fighter1.health / fighter2.damage_per_attack)
    f2 = math.ceil(fighter2.health / fighter1.damage_per_attack)
    if f1 == f2:
        return first_attacker
    else:
        return fighter1.name if f1 > f2 else fighter2.name

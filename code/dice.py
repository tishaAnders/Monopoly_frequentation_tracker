import numpy as np


def doubles_check(a, b):
    doubles = False
    if a == b:
        doubles = True
    return doubles

def jail_by_doubles(a, b, c):
    return a and b and c

def go_to_jail(move_no, current_pos, a, b, c):
    boo = False
    if move_no>1:
        if jail_by_doubles(a, b, c) == True:
            boo = True
        elif current_pos == 30:
            boo = True
    return boo

class rollDice:
    def __init__(self, result_1, result_2):
        self.result_1 = result_1
        self.result_2 = result_2
        self.result = result_1 + result_2
        self.doubles = doubles_check(result_1, result_2)



# roll1 = rollDice()
# print(roll1.result_1)
# print(roll1.result_2)
# print(roll1.result)
# print(roll1.doubles)

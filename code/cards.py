from __future__ import division
import numpy as np
import random
import math

monopoly_board = ["Go", "brown_1", "cc_1", "brown_2", "income_tax", "station_1", "light_blue_1", "chance_1", "light_blue_2", "light_blue_3", "prison_field",
"pink_1", "electric_c", "pink_2", "pink_3", "station_2", "orange_1", "cc_2", "orange_2", "orange_3", "free_parking",
"red_1", "chance_2", "red_2", "red_3", "station_3", "yellow_1", "yellow_2", "water_works", "yellow_3", "go_to_jail",
"green_1", "green_2", "cc_3", "green_3", "station_4", "chance_3", "dark_blue_1", "luxury_tax", "dark_blue_2"]
chance_card_stack = [0, 24, 11, 999, 10, 5, 15, 39, 1, 777, 777, 777, 777, 777, 777, 777]
cc_card_stack = [0, 777, 777, 777, 10, 777, 777, 777, 777, 777, 777, 777, 777, 777, 777, 777, 777]

def advance_to_next_station(pos):
    if (pos < 5 or pos > 35):
        return 5
    elif pos < 15:
        return 15
    elif pos < 25:
        return 25
    elif pos < 35:
        return 35


def draw_card(special_field, pos):
    if "cc" in special_field:
        print(" - community chest card has been drawn - ")
        num1 = np.random.randint(0,len(cc_card_stack))
        #print("random number out of stack: " + str(num1))
        advance_to = cc_card_stack[num1]
        if advance_to == 777:
            advance_to = pos
            print(" - no need to move - ")
            return 0
        else:
            print("- move forward " + str(advance_to-pos) + " steps - ")
            return advance_to - pos
    elif "chance" in special_field:
        print(" - chance card has been drawn - ")
        num2 = np.random.randint(0,len(chance_card_stack))
        advance_to = chance_card_stack[num2]
        if advance_to == 12: # nearest utility
            print("Advance to the next utility!")
            if pos <= 12:
                return 12 - pos
            else:
                return 28 - pos
        elif advance_to == 15: # nearest station
             print("Advance to the next station!")
             advance_to = advance_to_next_station(pos)
             return (advance_to - pos)%40
        elif advance_to == 999: # go back 3 spaces
            advance_to = pos-3
            print("Go back 3 spaces!")
            return - 3
        elif advance_to == 777: # no need to move
            advance_to = pos
            print(" - no need to move - ")
            return 0 # don't move anywhere
        else: # go straight to position XYZ
            print("Advance to " + monopoly_board[advance_to] + " !")
            return (advance_to - pos)%40


class card:
    def __init__(self, card_type, pos):
        self.card_type = card_type
        self.position = pos
        self.step_change = draw_card(card_type, pos)
        self.advance_to = (self.step_change + pos)%40

### main class of monopoly game
# defines the board,

import numpy as np
from dice import rollDice
from cards import card
from cards_silent import card_s
import dice
import random
from datetime import datetime
from matplotlib import pyplot as plt
import sys


monopoly_board = ["Go", "brown_1", "cc_1", "brown_2", "income_tax", "station_1", "light_blue_1", "chance_1", "light_blue_2", "light_blue_3", "prison_field",
"pink_1", "electric_c", "pink_2", "pink_3", "station_2", "orange_1", "cc_2", "orange_2", "orange_3", "free_parking",
"red_1", "chance_2", "red_2", "red_3", "station_3", "yellow_1", "yellow_2", "water_works", "yellow_3", "go_to_jail",
"green_1", "green_2", "cc_3", "green_3", "station_4", "chance_3", "dark_blue_1", "luxury_tax", "dark_blue_2"]

no_fields = len(monopoly_board)
landings_counter = []
for i in range(no_fields):
    landings_counter.append(0)
doubles_list = []
current_pos = 0
positions_list = []


def rolldie():
    return np.random.randint(1,7)

total_moves = int(input("How many times shall the dice be rolled? "))
print("Okay, the dice will be rolled " + str(total_moves) + " times.\n")
dicerolls = [rollDice(rolldie(), rolldie()) for move in range(total_moves)]

verbose_exec = input("Do you wish verbose execution? (Type 'yes' or 'no') ")


if verbose_exec == "no":
    for i in range(len(dicerolls)):
        #print("rolling result: " + str(dicerolls[i].result))
        doubles_list.append(dicerolls[i].doubles)
        #print("doubles? " + str(doubles_list[-1]))
        current_pos = (current_pos + dicerolls[i].result)%no_fields
        #print("current modulus:" + str(current_pos))
        positions_list.append(current_pos)
        #print("current position: " + monopoly_board[current_pos])
        landings_counter[current_pos] += 1
        if i>1 and Dice.go_to_jail(i, current_pos, doubles_list[-1], doubles_list[-2], doubles_list[-3]):
            #print("GO TO JAIL!")
            if positions_list[-1] != 30:
                positions_list = positions_list[:-1]
                landings_counter[current_pos] -= 1
            current_pos = 10
            #print("current position: " + monopoly_board[current_pos])
            positions_list.append(current_pos)
            landings_counter[current_pos] += 1
        elif "cc" in monopoly_board[current_pos]:
            #print("DRAW COMMUNITY CHEST CARD!")
            cc_card = card_s("cc", current_pos)
            #print("Do we need to move? " + str(cc_card.advance_to != current_pos))
            if cc_card.advance_to != current_pos:
                current_pos = cc_card.advance_to
                positions_list.append(current_pos)
            #print("current position: " + monopoly_board[current_pos])
            #landings_counter[current_pos] += 1
        elif "chance" in monopoly_board[current_pos]:
            #print("DRAW CHANCE CARD!")
            chance_card = card_s("chance", current_pos)
            #print("Do we need to move? " + str(chance_card.advance_to != current_pos))
            if chance_card.advance_to != current_pos:
                current_pos = chance_card.advance_to
                positions_list.append(current_pos)
            #print("current position: " + monopoly_board[current_pos])
        #print("_________________________________________")
elif verbose_exec == "yes":
        for i in range(len(dicerolls)):
            print("rolling result: " + str(dicerolls[i].result))
            doubles_list.append(dicerolls[i].doubles)
            print("doubles? " + str(doubles_list[-1]))
            current_pos = (current_pos + dicerolls[i].result)%no_fields
            #print("current modulus:" + str(current_pos))
            positions_list.append(current_pos)
            print("current position: " + monopoly_board[current_pos])
            landings_counter[current_pos] += 1
            if i>1 and Dice.go_to_jail(i, current_pos, doubles_list[-1], doubles_list[-2], doubles_list[-3]):
                print("GO TO JAIL!")
                if positions_list[-1] != 30:
                    positions_list = positions_list[:-1]
                    landings_counter[current_pos] -= 1
                current_pos = 10
                print("current position: " + monopoly_board[current_pos])
                positions_list.append(current_pos)
                landings_counter[current_pos] += 1
            elif "cc" in monopoly_board[current_pos]:
                print("DRAW COMMUNITY CHEST CARD!")
                cc_card = card("cc", current_pos)
                #print("Do we need to move? " + str(cc_card.advance_to != current_pos))
                if cc_card.advance_to != current_pos:
                    current_pos = cc_card.advance_to
                    positions_list.append(current_pos)
                print("current position: " + monopoly_board[current_pos])
            elif "chance" in monopoly_board[current_pos]:
                print("DRAW CHANCE CARD!")
                chance_card = card("chance", current_pos)
                #print("Do we need to move? " + str(chance_card.advance_to != current_pos))
                if chance_card.advance_to != current_pos:
                    current_pos = chance_card.advance_to
                    positions_list.append(current_pos)
                print("current position: " + monopoly_board[current_pos])
            print("_________________________________________")
else:
    print("Uh oh, a typo!")
    sys.exit("Execution has been stopped.")

print("_________________________________________")
print("_________________________________________")
print(str(total_moves) + " dice rolls have been executed.")

display_properties_only = input("Do you wish to see results for all spaces or for properties only? (Type 'a' or 'p') ")

colours = ["lightgrey", "saddlebrown", "palegreen", "saddlebrown", "lightgrey", "black", "deepskyblue", "palegreen", "deepskyblue", "deepskyblue", "lightgrey",
"magenta", "grey", "magenta", "magenta", "black", "orange", "palegreen", "orange", "orange", "lightgrey",
"red", "palegreen", "red", "red", "black", "yellow", "yellow", "grey", "yellow", "lightgrey",
"darkgreen", "darkgreen", "palegreen", "darkgreen", "black", "palegreen", "mediumblue", "lightgrey", "mediumblue"]

if display_properties_only == "a":
    print("Here's how many times you have landed on each space:")
    for i in range(len(monopoly_board)):
        print(str(monopoly_board[i]) + ": " + str(int(landings_counter[i])))
    plt.bar(monopoly_board,landings_counter, color=colours)
    plt.xticks(rotation=90)
    plt.xlabel("board squares")
    plt.ylabel("landings after " + str(total_moves) + " dice rolls")
    #plt.legend((monopoly_board), (colours))
    plt.title("Frequentation of squares in Monopoly board game, after " + str(total_moves) + " dice rolls" )
    plt.show()
elif display_properties_only == "p":
    non_property_positions = [0, 2, 4, 7, 10, 17, 20, 22, 30, 33, 36, 38]
    for i in range(len(non_property_positions)):
        non_property_positions[i] = non_property_positions[i] - i
    for non_property in non_property_positions:
        del monopoly_board[non_property]
        del landings_counter[non_property]
        del colours[non_property]
    print("Here's how many times you have landed on each space:")
    for i in range(len(monopoly_board)):
        print(str(monopoly_board[i]) + ": " + str(landings_counter[i]))
    plt.bar(monopoly_board,landings_counter, color=colours)
    plt.xticks(rotation=90)
    plt.xlabel("board squares")
    plt.ylabel("landings after " + str(total_moves) + " dice rolls")
    #plt.legend((monopoly_board), (colours))
    plt.title("Frequentation of squares in Monopoly board game, after " + str(total_moves) + " dice rolls" )
    plt.show()
else:
    sys.exit("Uh oh, a typo! Execution has been stopped.")

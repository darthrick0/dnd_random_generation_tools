import random
import pandas
import argparse
import os
import math
import numpy
from collections import Counter


parser = argparse.ArgumentParser(description='Enter Challenge Rating and recieve rolled rewards')
parser.add_argument('CR', help='Enter and integer greater than or equal to 1', type=int)
args = parser.parse_args()
# print(args.CR)

CR = args.CR
if CR < 1:
    raise ValueError('Challenge Rating must be greater than or equal to 1')


if CR <=4:
    individual_treasure_dataframe = pandas.read_excel('individual_treasure_tables.xlsx', sheet_name='CR 1-4', index_col='Roll')
elif CR <= 10:
    individual_treasure_dataframe = pandas.read_excel('individual_treasure_tables.xlsx', sheet_name='CR 5-10', index_col='Roll')
elif CR <= 16:
    individual_treasure_dataframe = pandas.read_excel('individual_treasure_tables.xlsx', sheet_name='CR 11-16', index_col='Roll')
else:
    individual_treasure_dataframe = pandas.read_excel('individual_treasure_tables.xlsx', sheet_name='CR 17+', index_col='Roll')


def roll_XdY_timesZ(x, y, z):
    total = 0
    for i in range(x):
        dice_roll = random.randint(1,y)
        print("roll in xd4 = " + str(dice_roll))
        total += dice_roll
    total = total * z
    #error check
    min_check = x * x * z
    max_check = x * y * z
    if min_check < total < max_check:
        total = -1

    return total

#--------------------------------------------------------
def coin_interpreter(number_to_roll):
    number_of_dice = number_to_roll[0:number_to_roll.find('d')]
    dice_type = number_to_roll[number_to_roll.find('d')+1:number_to_roll.find('x')]
    multiplier = number_to_roll[number_to_roll.find('x')+1:len(number_to_roll)]
    total = roll_XdY_timesZ(number_of_dice, dice_type, multiplier)
    return total

def read_coin_table_entry(row, column_list):
    for x in range(len(row)):
        if isinstance(row.get(x), str):
            # print(coin_row.get(x) + ' ' + column_list[x])
            print('total = ' + str(coin_interpreter(row.get(x))) + ' ' + column_list[x])
#--------------------------------------------------------


num_rows_in_coin = len(individual_treasure_dataframe)
coin_row = individual_treasure_dataframe.loc[CR]
# print(coin_row)
coin_column_list = individual_treasure_dataframe.columns.values.tolist()
read_coin_table_entry(coin_row, coin_column_list)
print('-------')



# for x in range(10):
#     val = roll_xd4(3)
#     print("total roll = " + str(val))
# print("----------------")

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

hoard_table_coins_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='Coins', index_col='CR')
if CR <=4:
    hoard_table_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='CR 1-4', index_col='Roll')
elif CR <= 10:
    hoard_table_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='CR 5-10', index_col='Roll')
elif CR <= 16:
    hoard_table_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='CR 11-16', index_col='Roll')
else:
    hoard_table_dataframe = pandas.read_excel('treasure_hoard_tables.xlsx', sheet_name='CR 17+', index_col='Roll')





#--------------------------------------------------------
def roll_XdY_timesZ(x, y, z):
    total = 0
    for i in range(int(x)):
        dice_roll = random.randint(1,int(y))
        # print("roll in xdy*z = " + str(dice_roll))
        total += dice_roll
    total = total * int(z)
    #error check
    # min_check = x * z
    # max_check = x * y * z
    # if min_check > total > max_check:
    #     total = -1
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



#--------------------------------------------------------
def read_hoard_table(row, column_list):
    for x in range(len(row)):
        if isinstance(row.get(x), str):
            # print(coin_row.get(x) + ' ' + column_list[x])
            # print(type(column_list[x]))
            if 'Art Object' in column_list[x]:
                print('Art Object Found')
            if 'Gems' in column_list[x]:
                print('Gems Found')
                # print(row.get(x))
                # print(type(column_list[x]))
                gem_entry_interpreter(row.get(x))
            if 'Magic Items' in column_list[x]:
                print('Magic Item Table Found')

def gem_entry_interpreter(entry):
    print('GEM INTERPRETER CALLED')
    reward_list = []
    number_of_dice = entry[0:entry.find('d')]
    dice_type = entry[entry.find('d')+1:entry.find('x')]
    total = roll_XdY_timesZ(number_of_dice, dice_type, 1)
    type_of_gem = entry[entry.find('x')+1:len(entry)]
    # print(type_of_gem)
    # print(type(type_of_gem))
    gem_dataframe = pandas.read_excel('individual_items.xlsx', sheet_name='Gems', index_col = 'Roll')
    number_of_rows = len(gem_dataframe.index)
    # print(number_of_dice + 'd' + dice_type + 'x' + type_of_gem)
    # print('column data type: ' + type(entry.columns(1)))
    gem_value_columns = gem_dataframe.columns.values.tolist()
    # print(total)
    # print(gem_value_columns)
    # print('number of columns: ' + str(len(gem_value_columns)))
    # # print(type(gem_value_columns))
    # print('total number of rolls: ' + str(total))


    for i in range(total):
        for j in range(len(gem_value_columns)):
            # print(j)
            # print('inside j')
            # print('gem_value_columns[j] = ' + str(gem_value_columns[j]) + ', type of gem is: ' + type_of_gem)
            if type_of_gem == str(gem_value_columns[j]):
                # print('inside if`')
                roll = roll_XdY_timesZ(1, number_of_rows, 1)
                # print('Roll Occured')
                # print(roll)
                # print('j = ' + str(j))
                # print(gem_dataframe.iloc[roll-1, j])
                reward_list.append(gem_dataframe.iloc[roll-1, j])
                # print(reward_list)
    reward_dict = Counter(reward_list)
    for gem in reward_dict:
        print(str(reward_dict[gem]) + ' x ' + gem)



def art_object_entry_interpreter(entry):
    # number_of_dice = entry[0:entry.find('d')]
    # dice_type = entry[entry.find('d')+1:entry.find('x')]
    # table = entry[entry.find('Table')+1:len(entry)]
    # total = roll_XdY_timesZ(number_of_dice, dice_type, 1)
    # return total
    print('art object function called')

def magic_item_entry_interpreter(entry):
    # number_of_dice = entry[0:entry.find('d')]
    # dice_type = entry[entry.find('d')+1:entry.find('x')]
    # type = entry[entry.find('x')+1:len(entry)]
    # total = roll_XdY_timesZ(number_of_dice, dice_type, 1)
    # return total
    print('magic item function called')
#--------------------------------------------------------


num_rows_in_coin = len(hoard_table_coins_dataframe)
coin_row = hoard_table_coins_dataframe.loc[CR]

#==
num_rows_in_hoard = len(hoard_table_dataframe)
roll_for_hoard_row = roll_XdY_timesZ(1,num_rows_in_hoard,1)
print('hoard random roll is: ' + str(roll_for_hoard_row))
item_row = hoard_table_dataframe.loc[roll_for_hoard_row]

# print(item_row)
hoard_column_list = hoard_table_dataframe.columns.values.tolist()
read_hoard_table(item_row, hoard_column_list)
print('-------')

# print(coin_row)
coin_column_list = hoard_table_coins_dataframe.columns.values.tolist()
read_coin_table_entry(coin_row, coin_column_list)
print('-------')

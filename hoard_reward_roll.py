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
def magic_item_entry_interpreter(entry):
    print('Magic Item Table Found')
    reward_list = []
    number_of_dice = entry[0:entry.find('d')]
    dice_type = entry[entry.find('d')+1:entry.find('x')]
    total = roll_XdY_timesZ(number_of_dice, dice_type, 1)
    table = entry[entry.find('x')+1:len(entry)]
    print(table)
    magic_item_table_dataframe = pandas.read_excel('magic_item_tables.xlsx', sheet_name=table, index_col = 'Roll')
    print(magic_item_table_dataframe)
    number_of_rows = len(magic_item_table_dataframe.index)
    table_value_columns = magic_item_table_dataframe.columns.values.tolist()

    # current implementation is hard coded to look at a single column
    for i in range(total):
        roll = roll_XdY_timesZ(1, number_of_rows, 1)
        reward_list.append(magic_item_table_dataframe.iloc[roll-1,0])

    # The following code could be used to condense the magic item tables rolling into one sheet or to add descriptions for each magic item.
    # Adding descriptions would be laborious right now and I dont feel like doing it.
    # for i in range(total):
    #     for j in range(len(table_value_columns)):
    #         if table == str(table_value_columns[j]):
    #             roll = roll_XdY_timesZ(1, number_of_rows, 1)
    #             reward_list.append(magic_item_table_dataframe.iloc[roll-1, j])


    print('Magic Items:')
    for magic_item in reward_list:
        print(magic_item)

def gem_entry_interpreter(entry):
    # print('Gems Found')
    reward_list = []
    number_of_dice = entry[0:entry.find('d')]
    dice_type = entry[entry.find('d')+1:entry.find('x')]
    total = roll_XdY_timesZ(number_of_dice, dice_type, 1)
    type_of_gem = entry[entry.find('x')+1:len(entry)]

    gem_dataframe = pandas.read_excel('individual_items.xlsx', sheet_name='Gems', index_col = 'Roll')
    number_of_rows = len(gem_dataframe.index)
    gem_value_columns = gem_dataframe.columns.values.tolist()
    for i in range(total):
        for j in range(len(gem_value_columns)):
            if type_of_gem == str(gem_value_columns[j]):
                roll = roll_XdY_timesZ(1, number_of_rows, 1)
                reward_list.append(gem_dataframe.iloc[roll-1, j])

    print('Gem Value: ' + type_of_gem + ' gp')
    reward_dict = Counter(reward_list)
    for gem in reward_dict:
        print(str(reward_dict[gem]) + ' x ' + gem)

def art_object_entry_interpreter(entry):
    print('Art Object Found')
    reward_list = []
    number_of_dice = entry[0:entry.find('d')]
    dice_type = entry[entry.find('d')+1:entry.find('x')]
    type_of_art_object = entry[entry.find('x')+1:len(entry)]
    print('dice: ' + number_of_dice + 'd' + dice_type  + 'x' +  type_of_art_object)
    total = roll_XdY_timesZ(number_of_dice, dice_type, 1)

    type_of_art_object = entry[entry.find('x')+1:len(entry)]
    # print('art_object type: ' + str(type_of_art_object))
    # print('number of rolls: ' + str(total))
    art_object_dataframe = pandas.read_excel('individual_items.xlsx', sheet_name='Art Objects', index_col = 'Roll')
    number_of_rows = len(art_object_dataframe.index)
    art_object_value_columns = art_object_dataframe.columns.values.tolist()
    for i in range(total):
        for j in range(len(art_object_value_columns)):
            if type_of_art_object == str(art_object_value_columns[j]):
                roll = roll_XdY_timesZ(1, number_of_rows, 1)
                reward_list.append(art_object_dataframe.iloc[roll-1, j])

    print('Art Object Value: ' + type_of_art_object + ' gp')
    reward_dict = Counter(reward_list)
    for art_object in reward_dict:
        print(str(reward_dict[art_object]) + ' x ' + art_object)


def read_hoard_table(row, column_list):
    for x in range(len(row)):
        if isinstance(row.get(x), str):
            if 'Art Object' in column_list[x]:
                art_object_entry_interpreter(row.get(x))
            if 'Gems' in column_list[x]:
                gem_entry_interpreter(row.get(x))
            if 'Magic Items' in column_list[x]:
                magic_item_entry_interpreter(row.get(x))


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

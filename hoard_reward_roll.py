import random
import pandas
import argparse
import os
import math



parser = argparse.ArgumentParser(description='Enter Challenge Rating and recieve rolled rewards')
parser.add_argument('CR', help='Enter and integer greater than or equal to 1', type=int)
args = parser.parse_args()
print(args.CR)

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
    for x in range(len(coin_row)):
        if isinstance(coin_row.get(x), str):
            # print(coin_row.get(x) + ' ' + column_list[x])
            print('total = ' + str(coin_interpreter(coin_row.get(x))) + ' ' + column_list[x])
#--------------------------------------------------------


num_rows_in_coin = len(hoard_table_coins_dataframe)
coin_row = hoard_table_coins_dataframe.loc[CR]


num_rows_in_hoard = len(hoard_table_dataframe)
roll_for_hoard_row = roll_XdY_timesZ(1,num_rows_in_hoard,1)
print('hoard random roll is: ' + str(roll_for_hoard_row))
item_row = hoard_table_dataframe.loc[roll_for_hoard_row]

print(item_row)
print('-------')
print(coin_row)
print('-------')
coin_column_list = hoard_table_coins_dataframe.columns.values.tolist()
read_coin_table_entry(coin_row, coin_column_list)

#
# print(column_list)
# print(type(column_list))
# for x in range(len(coin_row)):
#     if isinstance(coin_row.get(x), str):
#         print(coin_row.get(x) + ' ' + column_list[x])
#         print('total = ' + str(coin_interpreter(coin_row.get(x))) + ' ' + column_list[x])


    # print(type(coin_row.get(x)))
    # print(type(str(row.get(entry))))
    # output = str(row.get(x))









#---------------------------------------
def read_coin_table_entry(row, column_list):

    for x in range(len(coin_row)):
        if isinstance(coin_row.get(x), str):
            print(coin_row.get(x) + ' ' + column_list[x])
            print('total = ' + str(coin_interpreter(coin_row.get(x))) + ' ' + column_list[x])

    # for cell in row:
    #     if cell != null:
    #         reward = coin_entry_parser(cell)
    #         print('reward') #incorporate header, based on column

# def coin_entry_parser(cell):
#     string = str(cell)
#     number_of_dice = string[0:string.find('d')]
#     # dice_type = #d to x
#     # multiplier = #x to cell.len()
#     coin_total = roll_XdY_timesZ(number_of_dice, dice_type, multiplier)
#     return coin_total

#---------------------------------------
def read_hoard_reward_entry(row):
    for cell in row:
        if cell != null:
            reward = hoard_entry_parser(cell)
            print('reward') #incorporate header, based on column
    return -1

def hoard_entry_parser(cell):
    # number_of_dice = #0 to d
    # dice_type = #d to x
    return -1
#---------------------------------------



# print(row)
# print(row.size)
# for x in range(row.size):
#     print(row.get(x))
#     print(type(row.get(x)))
#     # print(type(str(row.get(entry))))
#     output = str(row.get(x))
